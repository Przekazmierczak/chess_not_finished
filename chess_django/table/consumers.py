import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Game, Board
from . import pieces

class TableConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.table_id = self.scope["url_route"]["kwargs"]["table_id"]
        self.table_group_id = "table_%s" % self.table_id

        # Join room group
        await self.channel_layer.group_add(self.table_group_id, self.channel_name)

        await self.accept()

        await self.send_actual_board()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.table_group_id, self.channel_name)


    async def send_actual_board(self):
        actual_board_array = await self.get_board_state_from_database()
        actual_board_object = pieces.create_json_board(actual_board_array)
        await self.send(text_data=json.dumps({"board": actual_board_object}))


    @sync_to_async
    def get_board_state_from_database(self):
        actual_game_db = Game.objects.get(pk=self.table_id)
        actual_board_db = Board.objects.filter(game=actual_game_db).latest('id')
        return json.loads(actual_board_db.board)['board']
    
    @sync_to_async
    def push_new_board_to_database(self, updated_board):
        game = Game.objects.get(pk=self.table_id)

        Board.objects.create(
            game = game,
            total_moves = 0,
            board = json.dumps({"board": updated_board}),
            turn = "w",
            castling = "----", # "kqKQ"
            soft_moves = 0
        )


    # # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        move = text_data_json["move"]

        old_board = await self.get_board_state_from_database()
        updated_board, correct = pieces.update_board(old_board, move)

        if correct:
            await self.push_new_board_to_database(updated_board)

            updated_json_board = pieces.create_json_board(updated_board)

            # Send message to room group
            await self.channel_layer.group_send(
                self.table_group_id, {"type": "new_board", "board": updated_json_board}
            )

    # Receive message from room group
    async def new_board(self, event):
        board = event["board"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"board": board}))
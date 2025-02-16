# from django.http import JsonResponse
import json
from django.shortcuts import render, redirect

from .models import Game, Board
from . import pieces

# Create your views here.
def index(request):
    return redirect("lobby_index")

def table(request, table_id):
    return render(request, "table/table_id.html", {
        "table_id": table_id,
    })

def create_table(request):
    new_game = Game.objects.create()

    table_id = f"{new_game.id}"
    return redirect("table", table_id=table_id)

def current(request):
    if request.user.is_authenticated and request.user.game:
        table_id = f"{request.user.game.id}"
        return redirect("table", table_id=table_id)
    else:
        return redirect("lobby_index")
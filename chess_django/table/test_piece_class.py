import unittest

from pieces import Piece

class Tests(unittest.TestCase):

    # initiate test board
    @classmethod
    def setUpClass(cls):
        cls.board = [[None for _ in range(8)] for _ in range(8)]

        cls.pieces_positions = [("pawn", "white", (1, 0)), ("pawn", "white", (2, 4)), ("pawn", "white", (1, 6)),
                                ("pawn", "black", (6, 3)), ("pawn", "black", (5, 4)), ("pawn", "black", (6, 7)),
                                ("rook", "white", (0, 0)), ("rook", "white", (5, 7)), ("rook", "black", (7, 0)), ("rook", "black", (7, 4)),
                                ("knight", "white", (2, 0)), ("knight", "white", (6, 4)), ("knight", "black", (7, 1)), ("knight", "black", (5, 5)),
                                ("bishop", "white", (4, 1)), ("queen", "white", (4, 3)), ("king", "white", (0, 4)), ("king", "black", (6, 6)),]

        for piece_position in cls.pieces_positions:
            piece, player, position = piece_position
            row, col = position

            cls.board[row][col] = Piece(piece, player, (row, col))


    def test_pawn_1_0(self):
        """Examine the movements of the pawn located on square (1, 0)."""
        self.assertEqual(self.board[1][0].check_possible_moves(self.board), ([], []))

    def test_pawn_2_3(self):
        """Examine the movements of the pawn located on square (2, 3)."""
        self.board[2][4].moved = True
        self.assertEqual(self.board[2][4].check_possible_moves(self.board), ([(3, 4)], []))

    def test_pawn_1_6(self):
        """Examine the movements of the pawn located on square (1, 6)."""
        self.assertEqual(self.board[1][6].check_possible_moves(self.board), ([(2, 6), (3, 6)], []))

    def test_pawn_6_3(self):
        """Examine the movements of the pawn located on square (6, 3)."""
        self.assertEqual(self.board[6][3].check_possible_moves(self.board), ([(5, 3)], []))

    def test_pawn_5_4(self):
        """Examine the movements of the pawn located on square (5, 4)."""
        self.board[5][4].moved = True
        self.assertEqual(self.board[5][4].check_possible_moves(self.board), ([(4, 4)], [(4, 3)]))

    def test_pawn_6_7(self):
        """Examine the movements of the pawn located on square (6, 7)."""
        self.assertEqual(self.board[6][7].check_possible_moves(self.board), ([], []))

    def test_rook_0_0(self):
        """Examine the movements of the rook located on square (0, 0)."""
        self.assertEqual(self.board[6][7].check_possible_moves(self.board), ([], []))

    def test_rook_0_0(self):
        """Examine the movements of the rook located on square (0, 0)."""
        self.assertEqual(self.board[0][0].check_possible_moves(self.board), ([(0, 1), (0, 2), (0, 3)], []))
        
    def test_rook_5_7(self):
        """Examine the movements of the rook located on square (5, 7)."""
        self.assertEqual(self.board[5][7].check_possible_moves(self.board), ([(4, 7), (3, 7), (2, 7), (1, 7), (0, 7), (5, 6)], [(6, 7), (5, 5)]))

    def test_rook_7_0(self):
        """Examine the movements of the rook located on square (7, 0)."""
        self.assertEqual(self.board[7][0].check_possible_moves(self.board), ([(6, 0), (5, 0), (4, 0), (3, 0)], [(2, 0)]))

    def test_rook_7_4(self):
        """Examine the movements of the rook located on square (7, 4)."""
        self.assertEqual(self.board[7][4].check_possible_moves(self.board), ([(7, 5), (7, 6), (7, 7), (7, 3), (7, 2)], [(6, 4)]))

    def test_knight_2_0(self):
        """Examine the movements of the knight located on square (2, 0)."""
        self.assertEqual(self.board[2][0].check_possible_moves(self.board), ([(0, 1), (3, 2), (1, 2)], []))

    def test_knight_6_4(self):
        """Examine the movements of the knight located on square (6, 4)."""
        self.assertEqual(self.board[6][4].check_possible_moves(self.board), ([(4, 5), (7, 6), (5, 6), (7, 2), (5, 2)], []))

    def test_knight_7_1(self):
        """Examine the movements of the knight located on square (7, 1)."""
        self.assertEqual(self.board[7][1].check_possible_moves(self.board), ([(5, 2), (5, 0)], []))

    def test_knight_5_5(self):
        """Examine the movements of the knight located on square (5, 5)."""
        self.assertEqual(self.board[5][5].check_possible_moves(self.board), ([(7, 6), (3, 6), (3, 4), (4, 7)], [(4, 3)]))

    def test_bishop_4_1(self):
        """Examine the movements of the bishop located on square (4, 1)."""
        self.assertEqual(self.board[4][1].check_possible_moves(self.board), ([(5, 2), (5, 0), (3, 2), (2, 3), (1, 4), (0, 5), (3, 0)], [(6, 3)]))
    
    def test_queen_4_3(self):
        """Examine the movements of the queen located on square (4, 3)."""
        self.assertEqual(self.board[4][3].check_possible_moves(self.board), ([(5, 3), (3, 3), (2, 3), (1, 3), (0, 3), (4, 4), (4, 5), (4, 6), 
                                                                              (4, 7), (4, 2), (5, 2), (6, 1), (3, 4), (2, 5), (3, 2), (2, 1)],
                                                                             [(6, 3), (5, 4), (7, 0)]))

    def test_king_0_4(self):
        """Examine the movements of the bishop located on square (0, 4)."""
        self.assertEqual(self.board[0][4].check_possible_moves(self.board), ([(1, 4), (0, 5), (0, 3), (1, 5), (1, 3)], []))

    def test_king_6_6(self):
        """Examine the movements of the bishop located on square (6, 6)."""
        self.assertEqual(self.board[6][6].check_possible_moves(self.board), ([(7, 6), (5, 6), (6, 5), (7, 7), (7, 5)], [(5, 7)]))

if __name__ == '__main__':
    unittest.main()
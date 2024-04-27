class TicTacToe:
    def __init__(self, n):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def make_move(self, row, col, player) -> int:
        self.board[row][col] = player
        won = self.has_won(row, col, player)
        if won:
            return player
        return 0
        
    def has_won(self, row, col, player) -> bool:
        if self.check_if_in_cross(row, col):
            if self.check_diag(player):
                return True

        return self.check_row(row, player) or self.check_col(col, player)

    def check_row(self, row, player) -> bool:
        for i in range(self.n):
            if self.board[row][i] != player:
                return False
        return True

    def check_col(self, col, player) -> bool:
        for i in range(self.n):
            if self.board[i][col] != player:
                return False
        return True

    def check_diag(self, player) -> bool:
        # Check forward
        forward = True
        for i in range(self.n): # 0,1,2,3,4,5
            if self.board[i][i] != player:
                forward= False
                break
        
        if forward: 
            return True

        # Check backward
        backward = True
        for i in range(self.n):
            if self.board[i][self.n - i - 1] != player:
                backward = False
                break

        return backward
        
    def check_if_in_cross(self, row, col) -> bool:
        return row == col or row + col == self.n - 1

    def print_board(self):
        for row in self.board:
            print(row)
    

import unittest

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        # players
        self.p1 = 1
        self.p2 = 2
        
        # outcomes
        self.no_winner = 0
        self.player_1_win = 1
        self.player_2_win = 2

    def test_column_win(self):
        """
        1, 0, 0
        1, 0, 0
        1, 0, 0
        """

        # Arrange
        game = TicTacToe(3)
        
        # Act
        move1 = game.make_move(0, 0, 1) # Not winner
        move2 = game.make_move(1, 0, 1) # Not winner
        move3 = game.make_move(2, 0, 1) # Player 1 winner
        
        # Assert
        self.assertEqual(move1, self.no_winner)
        self.assertEqual(move2, self.no_winner)
        self.assertEqual(move3, self.player_1_win)

        
    def test_row_win(self):
        """
        0, 0, 0
        1, 1, 1
        0, 0, 0
        """
        # Arrange
        game = TicTacToe(3)
        
        # Act
        move1 = game.make_move(1, 0, 1) # Not winner
        move2 = game.make_move(1, 1, 1) # Not winner
        move3 = game.make_move(1, 2, 1) # Player 1 winner
        
        # Assert
        self.assertEqual(move1, self.no_winner)
        self.assertEqual(move2, self.no_winner)
        self.assertEqual(move3, self.player_1_win)

    
    def test_diag_win(self):
        """
        1, 0, 0
        0, 1, 0
        0, 0, 1
        """
        # Arrange
        game = TicTacToe(3)
        
        # Act
        move1 = game.make_move(0, 0, 1) # Not winner
        move2 = game.make_move(1, 1, 1) # Not winner
        move3 = game.make_move(2, 2, 1) # Player 1 winner
        
        # Assert
        self.assertEqual(move1, self.no_winner)
        self.assertEqual(move2, self.no_winner)
        self.assertEqual(move3, self.player_1_win)

    def test_diag_win(self):
        """
        1, 0, 0
        0, 1, 0
        0, 0, 1
        """
        # Arrange
        game = TicTacToe(3)
        
        # Act
        move1 = game.make_move(0, 0, 1) # Not winner
        move2 = game.make_move(1, 1, 1) # Not winner
        move3 = game.make_move(2, 2, 1) # Player 1 winner
        
        # Assert
        self.assertEqual(move1, self.no_winner)
        self.assertEqual(move2, self.no_winner)
        self.assertEqual(move3, self.player_1_win)

    def test_rev_diag_win(self):
        """
        0, 0, 1
        0, 1, 0
        1, 0, 0
        """
        # Arrange
        game = TicTacToe(3)
        
        # Act
        move1 = game.make_move(0, 2, 1) # Not winner
        move2 = game.make_move(1, 1, 1) # Not winner
        move3 = game.make_move(2, 0, 1) # Player 1 winner
        
        # Assert
        self.assertEqual(move1, self.no_winner)
        self.assertEqual(move2, self.no_winner)
        self.assertEqual(move3, self.player_1_win)
        
    def test_mult_player_alt(self):
        """
        1, 2, 1
        1, 2, 2
        1, 0, 0
        """
        # Arrange
        game = TicTacToe(3)
        
        # Act & Assert
        self.assertEqual(game.make_move(0, 0, self.p1), self.no_winner) 
        self.assertEqual(game.make_move(1, 2, self.p2), self.no_winner) 
        self.assertEqual(game.make_move(0, 2, self.p1), self.no_winner) 
        self.assertEqual(game.make_move(1, 2, self.p2), self.no_winner) 
        self.assertEqual(game.make_move(1, 0, self.p1), self.no_winner) 
        self.assertEqual(game.make_move(0, 1, self.p2), self.no_winner) 
        self.assertEqual(game.make_move(2, 0, self.p1), self.player_1_win) 


if __name__ == '__main__':
    unittest.main()
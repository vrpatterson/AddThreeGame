import unittest
from AddThreeGame import AddThreeGame

class TestAddThreeGame(unittest.TestCase):
# A collection of tests that ensure AddThreeGame works properly

    def test_check_state_2_moves(self):
        game = AddThreeGame()
        game.make_move("Player_A", 2)
        game.make_move("Player_B", 5)
        state = game.get_curr_state()
        self.assertEqual(state, "UNFINISHED")

    def test_selection_too_large(self):
        game = AddThreeGame()
        player = "Player_A"
        selected_num = 10
        valid_move = game.check_valid_move(player, selected_num)
        self.assertFalse(valid_move)

    def test_selection_too_small(self):
        game = AddThreeGame()
        player = "Player_A"
        selected_num = 0
        valid_move = game.check_valid_move(player, selected_num)
        self.assertFalse(valid_move)       

    def test_valid_curr_player_after_move(self):
        game = AddThreeGame()
        game.make_move("Player_A", 3)
        current_turn = game.get_curr_turn()
        self.assertEqual(current_turn, 'Player_B')

    def test_move_already_taken(self):
        game = AddThreeGame()
        game.make_move("Player_A", 3)
        invalid_move = game.make_move("Player_B", 3)
        self.assertFalse(invalid_move)

    def test_attempt_playerB_first_move(self):
        game = AddThreeGame()
        first_move = game.make_move("Player_B", 2)
        self.assertFalse(first_move)

    def test_win_with_last_available_number(self):
        game = AddThreeGame()
        game.make_move("Player_A", 3)
        game.make_move("Player_B", 1)
        game.make_move("Player_A", 4)
        game.make_move("Player_B", 9)
        game.make_move("Player_A", 7)
        game.make_move("Player_B", 8)
        game.make_move("Player_A", 6)
        game.make_move("Player_B", 2)
        game.make_move("Player_A", 5)
        winner = game.get_curr_state()
        self.assertEqual(winner, "Player_A has won!")

    def test_playerB_win(self):
        game = AddThreeGame()
        game.make_move("Player_A", 3)
        game.make_move("Player_B", 5)
        game.make_move("Player_A", 1)
        game.make_move("Player_B", 2)
        game.make_move("Player_A", 9)
        game.make_move("Player_B", 8)
        winner = game.get_curr_state()
        self.assertEqual(winner, "Player_B has won!")

    def test_move_after_win(self):
        game = AddThreeGame()
        game.make_move("Player_A", 3)
        game.make_move("Player_B", 5)
        game.make_move("Player_A", 1)
        game.make_move("Player_B", 2)
        game.make_move("Player_A", 9)
        game.make_move("Player_B", 8) # winning move
        invalid_move = game.make_move("Player_A", 7)
        self.assertFalse(invalid_move)

    def test_draw(self):
        game = AddThreeGame()
        game.make_move("Player_A", 2)
        game.make_move("Player_B", 5)
        game.make_move("Player_A", 4)
        game.make_move("Player_B", 6)
        game.make_move("Player_A", 8)
        game.make_move("Player_B", 3)
        game.make_move("Player_A", 1)
        game.make_move("Player_B", 9)
        game.make_move("Player_A", 7)
        state = game.get_curr_state()
        self.assertEqual(state, "DRAW")

if __name__ == '__main__':
    unittest.main()

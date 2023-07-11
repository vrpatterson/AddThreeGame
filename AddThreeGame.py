# Victoria Patterson
# Updated Project 9 for OSU CS-161

# Project Description: 
# 'AddThreeGame' allows two players to play a game in which they alternately choose
# numbers from 1 - 9. They may not choose a number that has already been selected by
# either player. If at any point, exactly three of the player's numbers sum to exactly
# 15, then that player has won. If all numbers from 1 - 9 are chosen, but neither
# player has won, then the game ends in a draw. Player "A" has the first turn.

from itertools import combinations

class AddThreeGame:

    def __init__(self):
        self._player_A_nums = []
        self._player_B_nums = []
        self._curr_state = "UNFINISHED"
        self._curr_turn = "Player_A"

    def get_curr_state(self):
        return self._curr_state
    
    def get_curr_turn(self):
        return self._curr_turn
    
    def make_move(self, player, selected_num):
        # Check that move meets requirements
        if not self.check_valid_move(player, selected_num):
            return False

        # Record Move
        if player == "Player_A":
            self._player_A_nums.append(selected_num)
            self._curr_turn = "Player_B"
        else:
            self._player_B_nums.append(selected_num)
            self._curr_turn = "Player_A"

        # Check if game is completed
        if self.check_if_won(player):
            return True

    def check_valid_move(self, player, selected_num):
    # Helper function to ensure player attempting move is allowed to make move
        if player != self._curr_turn:       # Not players turn yet
            print("Not your turn")
            return False
        if selected_num < 1 or selected_num > 9:    # selected number is out of range
            print("Number selection is out of range")
            return False
        if selected_num in self._player_A_nums or selected_num in self._player_B_nums:      # selected number already chosen
            print("Number selection has already been chosen")
            return False
        if self._curr_state != "UNFINISHED":    # game has ended
            print("The game is already over...")
            return False
        
        # valid move
        return True
                    
    def check_if_won(self, player):
        target_value = 15
        num_valid_selections = 9
        if player == "Player_A":
            check_nums = self._player_A_nums
        else:
            check_nums = self._player_B_nums

        # Check for winning combination
        for combo in combinations(check_nums, 3):
            if sum(combo) == target_value:
                self._curr_state = player + " has won!"   # update the current state if player reaches target value
                self._curr_turn = player
                print('Game over!')
                return True
            
        # Check for draw  
        if len(self._player_A_nums) + len(self._player_B_nums) == num_valid_selections:
            self._curr_state = "DRAW"
            self._curr_turn = "None"
            print("All available numbers have been chosen")
            return True
        
        return False

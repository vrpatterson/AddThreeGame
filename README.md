# AddThreeGame  
  
A game created for OSU Computer Science I class Spring 2020 - reworked in July 2023  
  
# Project Description:  
'AddThreeGame' allows two players to play a game in which they alternately choose  
numbers from 1 - 9. They may not choose a number that has already been selected by  
either player. If at any point, exactly three of the player's numbers sum to exactly  
15, then that player has won. If all numbers from 1 - 9 are chosen, but neither  
player has won, then the game ends in a draw. Player "A" has the first turn.  
  
# How to play:  
Initialize game:  
&nbsp; &nbsp; &nbsp; game = AddThreeGame()  
    
Player_A has the first move:  
&nbsp; &nbsp; &nbsp; game.make_move("Player_A", 3)  
  
Player_B makes the next move:  
&nbsp; &nbsp; &nbsp; game.make_move("Player_B", 1)  
  
Continue until either player wins or there is a draw  
Results are printed to the console  

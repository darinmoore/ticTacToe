# 
# Filename: ticTacToe.py
# Author: Darin Moore
# Date: 9-6-16
# Description: Creates a game of tic-tac-toe against a simple AI
#

import random # for deciding whether computer or user makes first move

"""
  Function name: drawBoard(gameBoard)
  Parameters: gameBoard - The board containing the history of the player's and
                          AI's moves
  Description: Prints out the game board
  Return Value: None

"""
def drawBoard(gameBoard):
  # Prints top 3 boxes
  print "   |   |   "
  print " " + gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2]
  print "   |   |   "
  
  # Prints border between top and middle rows
  print "-----------"
  
  # Prints middle 3 boxes
  print "   |   |   "
  print " " + gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5]
  print "   |   |   "
  
  # Prints border between middle and bottom rows
  print "-----------"

  # Prints bottom 3 boxes
  print "   |   |   "
  print " " + gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8]
  print "   |   |   "


"""
  Function name: switchPlayer()
  Parameters: None
  Description: Switches the turn between the computer and the user
  Return Value: None

"""
def switchPlayer():
  # If currently user turn, switches to computer turn 
  if (playerTurn == 1):
    playerTurn = 0
  
  # If currently computer turn, switches to user turn
  else:
    playerTurn = 1


"""
  Function name: notOccupied(move, gameBoard)
  Parameters: move - space that the user is trying to occupy
              gameBoard - array containing all moves and open spaces
  Description: Checks to see if the space being chosen is open 
  Return Value: True - if the space is unoccupied
                False - if the space is occupied

"""
def notOccupied(move, gameBoard):
  boardPosition = move - 1
  
  # If space is not occupied, it returns true
  if (gameBoard[boardPosition] != 'X' and gameBoard[boardPosition] != 'O'):
    return True

  # If space is occupied, it returns false
  else:
    return False

"""
  Function name: compMove()
  Parameters: 
  Description: 
  Return Value: 

"""


"""
  Function name: main() 
  Parameters: None
  Description: Drives the main program, allows the user to play tic-tac-toe
  Return Value: None

"""
if __name__ == '__main__':
  # Prints welcome message for the user
  print "Welcome to tic-tac-toe!"
  
  # loops until a valid char is chosen
  while(True):  
    # Player chooses 'X' or 'O' for their moves
    playerChar = raw_input("Which side would you like to be? ('X' or 'O') ") 
    playerChar = playerChar.upper()

    # If player chooses 'X', it sets the computer to 'O'
    if (playerChar == 'X' or playerChar == 'x'):
      compChar = 'O'
      break

    # If player chooses 'O', it sets the computer to 'X'
    elif (playerChar == 'O' or playerChar == 'o'):
      compChar = 'X'
      break
    
    # If player doesn't choose 'X' or 'O'
    print "Not a valid option"

  # Contains all possible positions for moves
  gameBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  
  # Draws the blank board
  drawBoard(gameBoard)

  # Randomly choose who goes first, 0 is computer, 1 is user
  # TODO uncomment: 
  # playerTurn = random.randint(0,1)
  
  playerTurn = 1

  # Executes until game is complete
  while(True):
    # If it is the computer's turn, then it makes it's move
    if (playerTurn == 0):
      # move = compMove(gameBoard)
      print "Computer move"
      
    # Otherwise, it is the user's turn to make it's move
    else:
      # loops until valid number is chosen
      while(True):
        move = int(raw_input("Where would you like to go? (1-9): "))
 
        # Moves on to the next step if the chosen space is not occupied
        if (move >= 0 and move <= 9 and notOccupied(move, gameBoard) == True):
	  break

        print "Not a valid option"
      
      # Adds user's move to gameBoard in the correct location
      gameBoard[move - 1] = playerChar
    

    # Draws the updated board
    drawBoard(gameBoard)

    # ends game if someone has won
    # if (gameFinished(gameBoard) == True):
      # break







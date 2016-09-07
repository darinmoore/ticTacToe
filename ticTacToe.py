# 
# Filename: ticTacToe.py
# Author: Darin Moore
# Date: 9-6-16
# Description: Creates a game of tic-tac-toe against a simple AI
#


"""
  Function name: drawBoard(gameBoard)
  Parameters: gameBoard - The board containing the history of the player's and
                          AI's moves
  Description: Prints out the game board
  Return Value: None

"""
def drawBoard(board):
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
  Function name: playerCharChoice()
  Parameters: 
  Description: 
  Return Value: 

"""


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

  # Player chooses 'X' or 'O' for their moves
  playerChar = raw_input("Which side would you like to be? ('X' or 'O') ")
  
  # Contains all possible positions for moves
  gameBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  
  # Draws the blank board
  drawBoard(gameBoard)

 
  # Randomly choose who goes first



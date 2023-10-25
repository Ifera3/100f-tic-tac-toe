#!python3

def displayString(board):
  countr = 0
  """
  function should create a string that can be displayed using a print command
  this function should have no actual print commands in it
  
  input:
  list board: the game board data:
  7 8 9
  4 5 6
  1 2 3
  
  eg 
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  should display:
  - - X
  X O -
  O - -
  
  return value
  str the gameboard
  """
  boardToPrint = (6,7,8,3,4,5,0,1,2)
  display = ""
  for i in boardToPrint:
    if board[i] == 0:
      display = display + "-"
    elif board[i] == "X":
      display = display + "X"
    elif board[i] == "O":
      display = display + "O"
    countr = countr + 1
    if countr == 3 or countr == 6:
      display = display + "\n"
    elif i == 2:
      continue
    else:
      display = display + " "
  print(f'=====\n{display}\n=====')
  return display

def main():
  board = [ 'O' , 0 , 0 , 'X' , 'O' , 0 , 0 , 0 , 'X' ] 
  assert displayString(board) == "- - X\nX O -\nO - -"
  board = [ 0 , 'O' , 'X' , 'O' , 'O' , 0 , 'X' , 0 , 'X' ] 
  assert displayString(board) == "X - X\nO O -\n- O X"

if __name__ == "__main__":
  main()
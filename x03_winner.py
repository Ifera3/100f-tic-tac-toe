#!python3

"""
Create a function that will determine if one person is the winner (has 3 in a row)
inputs:
list board : the list that contains the board data

return:
str 'X' if X is the winner
str 'O' if O is the winner
None if there is no winner
6 7 8
3 4 5
0 1 2
"""
def center(board):
  player = board[4]
  a = (6,7,8,5)
  b = (2,1,0,3)
  for i in range(4):
    if (board[a[i]] == player and board[b[i]] == player) and (board[a[i]] != 0 and board[b[i]] != 0):
      #Sprint(player)
      return player
  else:
    #print('')
    return None

def strights(board):
  player = board[6]
  a = (3,7)
  b = (0,8)
  for i in range(2):
    if (board[a[i]] == player and board[b[i]] == player) and (board[a[i]] != 0 and board[b[i]] != 0):
      #print(player)
      return player
  else:
    #print('')
    player = board[2]
    a = (1,5)
    b = (0,8)
    for i in range(2):
      if (board[a[i]] == player and board[b[i]] == player) and (board[a[i]] != 0 and board[b[i]] != 0):
        #print(player)
        return player
    else:
      #print('')
      return None

def whoWins(board):
  if center(board) != None:
    return center(board)
  else:
    return strights(board)


def main():
  board = [ 'O','X',0,'X','O',0,'X',0,'O']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','O','X','O','O','X']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','X','O','O','X','O']
  assert whoWins(board) == None
  board = [ 'X','O',0,'X','X','X','O','O','X']
  assert whoWins(board) == 'X'

if __name__ == "__main__":
  main()

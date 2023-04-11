import random

print(""" 
Welcome HUMBLE USER , WE HOPE YOU WILL ENJOY THE ...!
""")
print(""" 
     _____  _  ____     _____  ____  ____     _____  ____  _____         
    /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/ 
      / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \ 
      | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   
      \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\ 


""")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
horizontal = 3
vertical = 3

def displayField():
  """ 
  A function that sets the field that iterates through,
  Sets the boundaries and core positions of the game
  """ 
  for x in range(horizontal):
    print('\n+---+---+---+')
    print('|', end='')
    for y in range(vertical):
      print('', field[x][y], end=' |')
  print('\n+---+---+---+')


def inputInArray(num, turn):
  """ 
  Function that identifies the field against the players choice
  Used for both determining the winner function and running the game 
  """
  num -= 1
  if (num == 0):
    field[0][0] = turn
  elif (num == 1):
    field[0][1] = turn
  elif (num == 2):
    field[0][2] = turn
  elif (num == 3):
    field[1][0] = turn
  elif (num == 4):
    field[1][1] = turn
  elif (num == 5):
    field[1][2] = turn
  elif (num == 6):
    field[2][0] = turn
  elif (num == 7):
    field[2][1] = turn
  elif (num == 8):
    field[2][2] = turn


def checkWhoWon(field):
  # A function that indentifies the winner of the game Includes X Axis Y Axis and Horizontal
  
  ### X Axis
  if (field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X'):
    print('X has won!')
    return True
  elif (field[0][0] == 'O' and field[0][1] == 'O' and field[0][2] == 'O'):
    print('O has won!')
    return True
  elif (field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X'):
    print('X has won!')
    return True
  elif (field[1][0] == 'O' and field[1][1] == 'O' and field[1][2] == 'O'):
    print('O has won!')
    return True
  elif (field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X'):
    print('X has won!')
    return True
  elif (field[2][0] == 'O' and field[2][1] == 'O' and field[2][2] == 'O'):
    print('O has won!')
    return True

  ### Y Axis
  elif (field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X'):
    print('X has won!')
    return True
  elif (field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O'):
    print('O has won!')
    return True
  elif (field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X'):
    print('X has won!')
    return True
  elif (field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O'):
    print('O has won!')
    return True
  elif (field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X'):
    print('X has won!')
    return True
  elif (field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O'):
    print('O has won!')
    return True
  ### Cross  wins
  elif (field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X'):
    print('X has won!')
    return True
  elif (field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O'):
    print('O has won!')
    return True
  elif (field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X'):
    print('X has won!')
    return True
  elif (field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O'):
    print('O has won!')
    return True
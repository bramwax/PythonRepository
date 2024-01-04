# Chess pieces and their points value are stored in a 1D array.
# The state of the unfinished chess game is stored in a 2D array.
NAMES = ["Pawn","Bishop","Knight","Rook","Queen"]
PIECES = ["P",1,"B",3,"K",3,'R',5,"Q",9]
BOARD = [["RW","KW","BW","*W","QW","BW","KW","RW"],
         ["PW","PW","PW","PW","PW","PW","PW","PW"],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["PB","PB","PB","PB","PB","PB","PB","PB"],
         ["RB","KB","BB","*B","QB","BB","KB","RB"]]


# Write an algorithm that prints out the name and points value of each chess piece
for i in range(0, 10, 2): # Numerical solution
  print(f"A {NAMES[i // 2]} is worth {PIECES[i + 1]}")

# for i in NAMES: # String solution
#   print(f"A {i} is worth {PIECES.index(i[0]) + 1}")


# Write an algorithm that counts the number of pieces remaining on the board, for
# each player. The winner of the game is the player with the most pieces. If no
# winner is found, the points for each of the players pieces are added together
# to determine the winner.
w_pieces, w_points, b_pieces, b_points = 0, 0, 0, 0

for row in range(0, 8):
  for col in range(0, 8):
    piece = BOARD[row][col][0]
    if piece != "*" and piece != " ":
      player = BOARD[row][col][1]
      if player == "W":
        w_pieces += 1
        w_points += PIECES[PIECES.index(piece)+1]
      else:
        b_pieces += 1
        b_points += PIECES[PIECES.index(piece)+1]

if w_pieces + w_points == b_pieces + b_points:
  print("The game is a draw...")
elif w_pieces > b_pieces:
  print(f"White is the winner with {w_pieces}...")
elif b_pieces > w_pieces:
    print(f"Black is the winner with {b_pieces}.")
elif w_points > b_points:
  print(f"White is the winner with {w_points} points.")
else:
  print(f"Black is the winner with {b_points} points.")

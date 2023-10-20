def draw_board(grid_vals):
  board = (f"|{grid_vals[1]}|{grid_vals[2]}|{grid_vals[3]}|\n"
             f"|{grid_vals[4]}|{grid_vals[5]}|{grid_vals[6]}|\n"
             f"|{grid_vals[7]}|{grid_vals[8]}|{grid_vals[9]}|")
  print(board)


def chk_turn(turn):
  if turn % 2 == 0: return 'O'
  else: return 'X'

def chk_for_win(grid_vals):
  # Handle Horizontal Cases
  if   (grid_vals[1] == grid_vals[2] == grid_vals[3]) \
    or (grid_vals[4] == grid_vals[5] == grid_vals[6]) \
    or (grid_vals[7] == grid_vals[8] == grid_vals[9]):
    return True
  # Handle Vertical Cases
  elif   (grid_vals[1] == grid_vals[4] == grid_vals[7]) \
    or (grid_vals[2] == grid_vals[5] == grid_vals[8]) \
    or (grid_vals[3] == grid_vals[6] == grid_vals[9]):
    return True
  # Diagonal Cases
  elif (grid_vals[1] == grid_vals[5] == grid_vals[9]) \
    or (grid_vals[3] == grid_vals[5] == grid_vals[7]):
    return True
    
  else: return False
g_vals = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

#required featues
playing, complete = True, False
turn = 0
prev_turn = -1


# Loop
while playing:
    #Game Board
    draw_board(g_vals)
    # If an invalid turn occurred, let the player know
    if prev_turn == turn:
      print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your position or press q to quit")
    
    # Get input and make sure it's valid
    choice = input()
    # The game has ended, 
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in g_vals:
      # Check if the spot is already taken.
        if not g_vals[int(choice)] in {"X", "O"}:
            turn += 1
            g_vals[int(choice)] = chk_turn(turn)
      
    # Check if the game results
    if chk_for_win(g_vals): playing, complete = False, True
    if turn > 8: playing = False
    
# Update the board.
draw_board(g_vals)
# If there was a winner, say who won
if complete:
  if chk_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("Player 2 Wins!")
else: 
  # Tie Game
  print("No Winner")
  
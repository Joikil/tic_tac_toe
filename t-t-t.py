#t-t-t
import os
#to check whose turn game start with "O"
def Chk_turn(t):
    if t%2 == 0: return 'O'
    else: return 'X'

#to check if game ends and find result
def chk_win(grid_vals):
    win_set = [   
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,1,2],
        [0,4,8],
        [2,4,6],
        [3,4,5],
        [6,7,8]
    ]
    for i in win_set:
        if(grid_vals[i[0]]==grid_vals[i[1]]==grid_vals[i[2]]):
            return True

#game board
g_vals = [1,2,3,4,5,6,7,8,9]
g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
         f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
         f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|")

G_on = True
turn = 0
complete= False
#loop begin
while G_on:
    os.system('cls' if os.name == 'nt' else 'clear')
    g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
         f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
         f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|")
    print(g_board)
    print("It's "+Chk_turn(turn+1)+" turn")
    choice = input("Enter the block number or  'q' to Quit:\n")
    if choice == 'q':
        G_on = False
    elif int(choice) in range(1,10) and not g_vals[int(choice)-1] in ['X','O']:
        turn += 1
        g_vals[int(choice)-1] = Chk_turn(turn)
    elif int(choice) not in g_vals:
        print("Invalid spot selected, please pick another.")
    if chk_win(g_vals): G_on, complete = False, True
    if turn > 8: G_on = False
 

g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
         f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
         f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|") 
print(g_board)
#if G_stat:#to print result
if complete:
    if turn%2 != 0: print("Player 'X' Wins!")
    else: print("Player 'O' Wins!")
else:
    #Tie Match
    print("No Winner, Match is Draw")

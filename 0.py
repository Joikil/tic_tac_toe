
'''g_vals = [1,2,3,4,5,6,7,8,9]


def Chk_turn(t):
    if t%2 == 0:return 'O'
    else: return 'X'

t=True
turn = 0

while t:
    g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
         f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
         f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|")
    print(g_board)
    print("It's "+Chk_turn(turn)+" turn")
    choice = input("Enter the block number:\n")
    if choice == 'q':
        G_on = False
    elif int(choice) in range(1,10) and not g_vals[int(choice)-1] in ['X','O']:
        turn += 1
        g_vals[int(choice)-1] = Chk_turn(turn)
    else :
        print("invalid input")
'''
#t-t-t

#to check whose turn game start with "O"
def Chk_turn(t):
    if t%2 == 0:return 'O'
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
'''
def chk_for_win(grid_vals):
  # Handle Horizontal Cases
    if (grid_vals[0] == grid_vals[1] == grid_vals[2]) \
        or (grid_vals[3] == grid_vals[4] == grid_vals[5]) \
        or (grid_vals[6] == grid_vals[7] == grid_vals[8]):
        return True
    # Handle Vertical Cases
    elif (grid_vals[0] == grid_vals[3] == grid_vals[6]) \
        or (grid_vals[1] == grid_vals[4] == grid_vals[7]) \
        or (grid_vals[2] == grid_vals[5] == grid_vals[8]):
        return True
    # Diagonal Cases
    elif (grid_vals[0] == grid_vals[4] == grid_vals[8]) \
        or (grid_vals[2] == grid_vals[4] == grid_vals[6]):
        return True

    else: return False
'''
    

#game board
g_vals = [1,2,3,4,5,6,7,8,9]
g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
         f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
         f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|")

         
"""win_set = [   
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,1,2],
    [0,4,8],
    [2,4,6],
    [3,4,5],
    [6,7,8]
]"""

G_on = True
turn = 0
complete= False
#loop begin

while G_on:
    Undo=False
    # Reset the screen
    g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
        f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
        f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|")
    print(g_board)
    print("It's "+Chk_turn(turn+1)+" turn")
    choice = input("Enter the block number or 'q' to Quit:\n")
    if choice == 'q':
        G_on = False
    elif int(choice) in range(1,10) and not g_vals[int(choice)-1] in ['X','O']:
        turn += 1
        g_vals[int(choice)-1] = Chk_turn(turn)
    else :
        print("Invalid input")
    #UNDO
    if not Undo:
        g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
        f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
        f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|")
        print(g_board)
        Undo=input("Enter 'u' to undo or Any_key to continue:")
        if Undo == "u":
            turn-=1
            g_vals[int(choice)-1]= int(choice)

    if chk_win(g_vals): G_on, complete = False, True
    if turn > 8: G_on = False
        
#print(complete)
g_board = (f"|{g_vals[0]}|{g_vals[1]}|{g_vals[2]}|\n"
        f"|{g_vals[3]}|{g_vals[4]}|{g_vals[5]}|\n"
        f"|{g_vals[6]}|{g_vals[7]}|{g_vals[8]}|")
print(g_board)
#if G_stat:#to print result
if complete:
    '''if Chk_turn(turn)_== 'X': print("Player 'X' Wins")'''"""It's showing error"""
    if turn%2 != 0: print("Player 'X' Wins!")
    else: print("Player 'O' Wins")
else:
    #Tie Match
    print("No Winner, Match is Draw")


   



    
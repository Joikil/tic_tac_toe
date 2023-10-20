from ttt_game import TicTacToeState,Action,Record,Sign,Turn

class TicTacToe:
    def __init__(self):
        self.state = TicTacToeState()
        
    def play(self):
        while not self.state.ended():
            self.display_board()
            action = self.get_player_move()
            self.state.dispatch(action)
            self.record.save_action_to_file(action,self.f_name)
        self.display_board()
        winner = self.state.winner()
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")
    def get_player_move(self):
        while True:
            try:
                i, j = map(int, input(f"Player {self.state.turn}, enter row and column (0-2) separated by a space: ").split())
                if 0 <= i <= 2 and 0 <= j <= 2 and self.state.board[i][j] == Sign._:
                    return Action((i, j))
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter two numbers (0-2) separated by a space.")

    def display_board(self): 
        for row in self.state.board:
            print(" ".join(str(sign.name) for sign in row))
            print()
        
game = TicTacToe()
game.play()
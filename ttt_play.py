import io
from ttt_game import TicTacToeState, Action, Sign, Turn, FileActionRecorder
import os.path


class TicTacToe:
    def __init__(self, file: io.FileIO):
        self.state = TicTacToeState()
        self.ar = FileActionRecorder(file=file)

    def play(self):
        while not self.state.ended():
            self.display_board()
            action = self.get_player_move()
            self.ar.record(action)
            self.state.dispatch(action)
            # self.record.save_action_to_file(action,self.f_name)
        self.display_board()
        winner = self.state.winner()
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")

    def get_player_move(self):
        while True:
            try:
                i, j = map(
                    int,
                    input(
                        f"Player {self.state.turn}, enter row and column (0-2) separated by a space: "
                    ).split(),
                )
                if 0 <= i <= 2 and 0 <= j <= 2 and self.state.board[i][j] == Sign._:
                    return Action((i, j))
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print(
                    "Invalid input. Please enter two numbers (0-2) separated by a space."
                )

    def display_board(self):
        if self.state.board == [[Sign._ for _ in range(3)] for _ in range(3)]:
            l = self.ar.moves()
            for a in l:
                self.state.dispatch(a)

        for row in self.state.board:
            print(" ".join(str(sign.name) for sign in row))
            print()


def main():
    with open("game.txt", "a+") as file:
        file.seek(0)
        game = TicTacToe(file=file)
        game.play()
        file.truncate(0)
    print("Game ended!")


if __name__ == "__main__":
    main()

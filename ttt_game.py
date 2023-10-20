import enum
import typing as t

class Sign(enum.IntEnum):
    _ = enum.auto()
    x = enum.auto()
    o = enum.auto()
1
class Turn(enum.IntEnum):
    x = enum.auto()
    o = enum.auto()

    def toggle(self):
        if self == Turn.x:
            return Turn.o
        return Turn.x

def sign_on_turn(turn: Turn):
    if turn == Turn.x:
        return Sign.x
    return Sign.o

class TicTacToeState:
    def __init__(self):
        self.board = [[Sign._ for _ in range(3)] for _ in range(3)]
        self.turn = Turn.x

    def dispatch(self, action):
        if self.ended():
            return
        i, j = action.square
        if self.board[i][j] != Sign._:
            return
        self.board[i][j] = sign_on_turn(self.turn)
        self.turn = self.turn.toggle()

    def ended(self) -> bool:
        return self.winner() is not None or all(all(cell != Sign._ for cell in row) for row in self.board)

    def winner(self) -> t.Optional[Turn]:
        for sign in (Sign.x, Sign.o):
            for i in range(3):
                if all(self.board[i][j] == sign for j in range(3)):
                    return Turn.x if sign == Sign.x else Turn.o
                if all(self.board[j][i] == sign for j in range(3)):
                    return Turn.x if sign == Sign.x else Turn.o
            if all(self.board[i][i] == sign for i in range(3)) or all(self.board[i][2 - i] == sign for i in range(3)):
                return Turn.x if sign == Sign.x else Turn.o
        return None

class Action:
    def __init__(self, square):
        self.square = square

class Record:
    def __init__(self):
        ...
    def save_action_to_file(self, action,x):
        with open(x, "a") as file:
            file.write(str(action.square[0])+" "+str(action.square[1])+"\n")
            file.close()

    def action_to_g_board(self,x):
        r=open(x,"r")
        l=[]
        for i in r:
            a,b=map(int,i.split())
            l.append((a,b))
        return l
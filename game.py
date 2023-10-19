import enum
import typing as t

class Sign(enum.IntEnum):
    _ = enum.auto()
    x = enum.auto()
    o = enum.auto()

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
        self.board = [ [Sign._ for _ in range(3) ] for _ in range(3) ]
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
        ...
    
    def winner(self) -> t.Optional[Turn]:
        if not self.ended():
            return None
        return self.turn.toggle()


class Action:
    def __init__(self, square):
        self.square = square   
    
    

class TicTacToe:
    def __init__(self):
        self.state = TicTacToeState()


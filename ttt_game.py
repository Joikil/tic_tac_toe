import enum
import typing as t
import sqlite3

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
        return self.winner() is not None or all(
            all(cell != Sign._ for cell in row) for row in self.board
        )

    def winner(self) -> t.Optional[Turn]:
        for sign in (Sign.x, Sign.o):
            for i in range(3):
                if all(self.board[i][j] == sign for j in range(3)):
                    return Turn.x if sign == Sign.x else Turn.o
                if all(self.board[j][i] == sign for j in range(3)):
                    return Turn.x if sign == Sign.x else Turn.o
            if all(self.board[i][i] == sign for i in range(3)) or all(
                self.board[i][2 - i] == sign for i in range(3)
            ):
                return Turn.x if sign == Sign.x else Turn.o
        return None


class Action:
    def __init__(self, square):
        self.square = square


import abc


class ActionRecorder(abc.ABC):
    @abc.abstractmethod
    def moves(self) -> t.List[Action]:
        pass

    @abc.abstractmethod
    def record(self, action: Action):
        ...
    
    #@abc.abstractmethod
    #def erase(self):


class SQLDatabaseActionRecorder(ActionRecorder):
    def __init__(self, conn: sqlite3.Connection)-> None:
        self._conn = conn
        self.cursor=self._conn.cursor()
        
    
    def moves(self) -> t.List[Action]:
        ...
        moves =self.cursor.execute("SELECT ACTION FROM MOVE;")
        actions=list(map(lambda i: Action((i[0]//3,i[0]%3)), moves))               
        return actions

    def record(self, action: Action):
        ...

        i, j = action.square
        val = i*3+j
        self.cursor.execute('''INSERT INTO MOVE (ACTION) VALUES (?)''',(val,))       
        self._conn.commit()




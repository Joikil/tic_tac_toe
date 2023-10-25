import enum
import typing as t
#import 

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

'''class Record:
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
'''

import abc
class ActionRecorder(abc.ABC):
    @abc.abstractmethod
    def moves(self) -> t.List[Action]:
        pass

    @abc.abstractmethod
    def record(self, action: Action):
        ...


class FileActionRecorder(ActionRecorder):
    def __init__(self, f) -> None:
        self.f=GFileControl(f)

    #Extracting from source
    def moves(self):
        ... 
        # f=open(self.f,"r")
        # r=open(self.f,"r")
        # content=f.read(1)
        #condition for empty file
        r=self.f.ReadData()
        l=[]
        if not r:
            pass
        else:
            for i in r:
                a,b=map(int,i.split())
                l.append((a,b))
        # r.close()
        return l
        ...

    #Adding into source
    def record(self,action):
        ...
        # file=open(self.f, "a")
        # file.write(str(action.square[0])+" "+str(action.square[1])+"\n")
        # file.close()
        self.f.WriteData(action)

  

class DataManager(abc.ABC):
    #@abc.abstractmethod
    #def OpenData(self):
    #    ...
    
    @abc.abstractmethod
    def ReadData(self) -> str:
        ...
    @abc.abstractmethod
    def WriteData(self,data):

        ...
    @abc.abstractmethod
    def Close(self,f):

        ...

class GFileControl(DataManager):
    def __init__(self,f):
        self.f=f
        self.file=open(self.f,"r+")

    def ReadData(self) -> str:
        if self.file:
            return self.file.read()
    def WriteData(self,data):
        if self.file:
            self.file.write(str(data.square[0])+" "+str(data.square[1])+"\n")
    def Close(self, f):
        self.file.close()
    
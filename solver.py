class SolvingMethod():
    def __init__(self, board):
        self.name = "Method"
        self.board = board
    def Solve(self):
        return
    def HelperSolve(self):
        return

class HiddenSingleMethod(SolvingMethod):
    def __init__(self, board):
        self.name = "Hidden Single Method"
        self.board = board
    def Solve(self):
        values=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                if j.default==False:
                    j.value="".join([t for t in values if t not in [k.value for k in i] and t not in [k[c2].value for k in self.board.tiles]])
                #print([k.value for k in i])
                #print([k[c2].value for k in self.board.tiles])


class Solver():
    def __init__(self, board):
        self.board = board
        self.solvingMethods=[]
        self.solvingMethods.append(HiddenSingleMethod(board))
    def Solve(self):
        for i in self.solvingMethods:
            i.Solve()
        print(self.board)
    def HelperSolve(self):
        for i in self.solvingMethods:
            i.HelperSolve()





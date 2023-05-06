class SolvingMethod():
    def __init__(self, board):
        self.name = "Method"
        self.description = "Reveals numbers in a magical way"
        self.board = board
        self.candidateschanged=False
        self.valuefound=False
        self.helperresponse=""
    def Solve(self, helper=False):
        return
    def HelperSolve(self, helper=False):
        self.Solve(helper=True)

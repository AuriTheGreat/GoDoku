from  solving_methods.SolvingMethod import SolvingMethod
import math

class CandidateTilesElimination(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Candidate Tiles Elimination"
        self.description = "The digit is the only possible candidate in the tile"

    def Solve(self):
        values=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                if j.value=="":
                    values_in_same_row=[k.value for k in i]
                    values_in_same_column=[k[c2].value for k in self.board.tiles]
                    values_in_same_box=[g.value for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                    newcandidatevalues="".join([t for t in values if t not in values_in_same_row and t not in values_in_same_column and t not in values_in_same_box])
                    if j.candidatevalues!=newcandidatevalues:
                        j.candidatevalues=newcandidatevalues
                        self.candidateschanged=True
                        if j.solecandidate():
                            self.valuefound=True
                #print([k.value for k in i])
                #print([k[c2].value for k in self.board.tiles])
        return False
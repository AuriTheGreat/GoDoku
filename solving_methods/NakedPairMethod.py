from  solving_methods.SolvingMethod import SolvingMethod
import math

class NakedPairMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Naked Pair Method"
        self.description = "There is a set of two candidate digits in two tiles in the same row/column/square, therefore eliminating them from the rest of row/column/square"
    def Solve(self):
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                tiles_in_same_row=i
                if self.FindPairs(tiles_in_same_row):
                    return True

                tiles_in_same_column=[k[c2] for k in self.board.tiles]
                if self.FindPairs(tiles_in_same_column):
                    return True

                tiles_in_same_box=[g for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                if self.FindPairs(tiles_in_same_box):
                    return True

        return False


    def FindPairs(self, candidatevalueset):
        existingpairs=[]
        for i in candidatevalueset:
            if len(i.candidatevalues)==2 and i.candidatevalues in existingpairs:
                changed=False
                for j in candidatevalueset:
                    if j.candidatevalues==i.candidatevalues:
                        continue
                    newvalues="".join([k for k in j.candidatevalues if k not in i.candidatevalues])
                    if j.candidatevalues!=newvalues:
                        self.candidateschanged=True
                        changed=True
                        j.candidatevalues=newvalues
                        if i.solecandidate():
                            self.valuefound=True
                if changed:
                    return True
            else:
                existingpairs.append(i.candidatevalues)
        return False
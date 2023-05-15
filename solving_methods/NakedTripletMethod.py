from  solving_methods.SolvingMethod import SolvingMethod
import math

class NakedTripletMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Naked Triplet Method"
        self.description = "There is a set of three candidate digits in three tiles in the same row/column/square, therefore eliminating them from the rest of row/column/square"
    def Solve(self):
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                tiles_in_same_row=i
                if self.FindTriplets(tiles_in_same_row):
                    return True

                tiles_in_same_column=[k[c2] for k in self.board.tiles]
                if self.FindTriplets(tiles_in_same_column):
                    return True

                tiles_in_same_box=[g for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                if self.FindTriplets(tiles_in_same_box):
                    return True
        return False


    def FindTriplets(self, candidatevalueset):
        potentialtriplets=[i for i in candidatevalueset if 1<len(i.candidatevalues)<4]
        for c1, a in enumerate(potentialtriplets):
            for c2, b in enumerate(potentialtriplets):
                if c1==c2:
                    continue
                for c3, c in enumerate(potentialtriplets):
                    if c1==c3 or c2==c3:
                        continue
                    if len(set(a.candidatevalues+b.candidatevalues+c.candidatevalues))==3:
                        changed=False
                        tripleset=sorted(set(a.candidatevalues+b.candidatevalues+c.candidatevalues))
                        for i in candidatevalueset:
                            if i!=a and i!=b and i!=c:
                                newvalues="".join([k for k in i.candidatevalues if k not in tripleset])
                                if i.candidatevalues!=newvalues:
                                    self.candidateschanged=True
                                    changed=True
                                    i.candidatevalues=newvalues
                                    if i.solecandidate():
                                        self.valuefound=True
                        if changed:
                            return True
        return False
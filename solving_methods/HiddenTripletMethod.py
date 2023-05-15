from  solving_methods.SolvingMethod import SolvingMethod
import math

#was accidentally created, was confused with naked subset methods, therefore is not used.
#is also buggy

class HiddenTripletMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Hidden Triplet Method"
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
        existingvalues={str(i):[] for i in range(1,10)}
        for i in candidatevalueset:
            for j in i.candidatevalues:
                    existingvalues[j].append(i)

        tripletvalues={i:existingvalues[i] for i in existingvalues if 1<len(existingvalues[i])<4}

        for c1, i in enumerate(tripletvalues):
            for c2, j in enumerate(tripletvalues):
                if c1==c2:
                    continue
                for c3, k in enumerate(tripletvalues):
                    if c1==c3 or c2==c3:
                        continue
                    valuelist=set(tripletvalues[i]+tripletvalues[j]+tripletvalues[k])

                    if len(valuelist)==3:
                        newvalues=sorted([i, j, k])
                        #print(newvalues)
                        changed=False
                        for i in valuelist:
                            replacingvalues="".join([k for k in i.candidatevalues if k not in newvalues])
                            if i.candidatevalues!=replacingvalues:
                                changed=True
                                i.candidatevalues=replacingvalues
                        #print("3", i, j, k, set(valuelist))
                        if changed:
                            return True

        return False
from  solving_methods.SolvingMethod import SolvingMethod
import math

#was accidentally created, was confused with naked subset methods, therefore is not used.

class HiddenPairMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Hidden Pair Method"
    def Solve(self, helper=False):
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
        #checks if:
        #1) there are only two cases of a value occuring in row/column/box
        #2) in those cases when there are two cases a value occurs in row/column/box, it also checks whether they occur
        #in the same squares
        existingvalues={str(i):[] for i in range(1,10)}
        for i in candidatevalueset:
            for j in i.candidatevalues:
                    existingvalues[j].append(i)

        pairvalues={i:existingvalues[i] for i in existingvalues if len(existingvalues[i])==2}
        pairvaluelists=[i for c1, i in enumerate(pairvalues.values()) for c2, j in enumerate(pairvalues.values()) if c1!=c2 and i==j]

        if pairvaluelists:
            newvalues="".join([i for i in pairvalues if pairvalues[i]==pairvaluelists[0]])
            changed=False
            for i in pairvaluelists[0]:
                if i.candidatevalues!=newvalues:
                    changed=True
                    i.candidatevalues=newvalues
            return changed

        return False
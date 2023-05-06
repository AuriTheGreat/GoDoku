from  solving_methods.SolvingMethod import SolvingMethod
import math

class HiddenSingleMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Hidden Single Method"
    def Solve(self, helper=False):
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                candidatevalues_in_same_row=[k.candidatevalues for k in i]
                numbers=self.FindSingles(candidatevalues_in_same_row)
                replacingvalue=[g for g in numbers if g in j.candidatevalues]
                if replacingvalue:
                    j.value=replacingvalue[0]
                    j.candidatevalues=""
                    self.valuefound=True
                    return True

                candidatevalues_in_same_column=[k[c2].candidatevalues for k in self.board.tiles]
                numbers=self.FindSingles(candidatevalues_in_same_column)
                replacingvalue=[g for g in numbers if g in j.candidatevalues]
                if replacingvalue:
                    j.value=replacingvalue[0]
                    j.candidatevalues=""
                    self.valuefound=True
                    return True

                candidatevalues_in_same_box=[g.candidatevalues for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                numbers=self.FindSingles(candidatevalues_in_same_box)
                replacingvalue=[g for g in numbers if g in j.candidatevalues]
                if replacingvalue:
                    j.value=replacingvalue[0]
                    j.candidatevalues=""
                    self.valuefound=True
                    return True

        return False


    def FindSingles(self, candidatevalueset):
        existingvalues={}
        singlevalues=[]
        for i in candidatevalueset:
            for j in i:
                if j in existingvalues:
                    existingvalues[j]+=1
                else:
                    existingvalues[j]=1
        for i in existingvalues:
            if existingvalues[i]==1:
                singlevalues.append(i)
        #print(candidatevalueset)
        #print(singlevalues)
        return singlevalues
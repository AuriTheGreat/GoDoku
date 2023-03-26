import math

class SolvingMethod():
    def __init__(self, board):
        self.name = "Method"
        self.board = board
    def Solve(self):
        return
    def HelperSolve(self):
        return
    def FindCandidateTiles(self):
        values=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                if j.value=="":
                    values_in_same_row=[k.value for k in i]
                    values_in_same_column=[k[c2].value for k in self.board.tiles]
                    values_in_same_box=[g.value for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                    j.candidatevalues="".join([t for t in values if t not in values_in_same_row and t not in values_in_same_column and t not in values_in_same_box])
                #print([k.value for k in i])
                #print([k[c2].value for k in self.board.tiles])

class HiddenSingleMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Hidden Single Method"
    def Solve(self):
        changed=True
        while changed:
            self.FindCandidateTiles()
            changed=False
            for c1, i in enumerate(self.board.tiles):
                for c2, j in enumerate(i):
                    if len(j.candidatevalues)==1:
                        changed=True
                        j.value=j.candidatevalues
                        j.candidatevalues=""
                        self.FindCandidateTiles()

                    candidatevalues_in_same_row=[k.candidatevalues for k in i]
                    numbers=self.FindSingles(candidatevalues_in_same_row)
                    replacingvalue=[g for g in numbers if g in j.candidatevalues]
                    if replacingvalue:
                        changed=True
                        j.value=replacingvalue[0]
                        j.candidatevalues=""
                        self.FindCandidateTiles()

                    candidatevalues_in_same_column=[k[c2].candidatevalues for k in self.board.tiles]
                    numbers=self.FindSingles(candidatevalues_in_same_column)
                    replacingvalue=[g for g in numbers if g in j.candidatevalues]
                    if replacingvalue:
                        changed=True
                        j.value=replacingvalue[0]
                        j.candidatevalues=""
                        self.FindCandidateTiles()

                    candidatevalues_in_same_box=[g.candidatevalues for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                    numbers=self.FindSingles(candidatevalues_in_same_box)
                    replacingvalue=[g for g in numbers if g in j.candidatevalues]
                    if replacingvalue:
                        changed=True
                        j.value=replacingvalue[0]
                        j.candidatevalues=""
                        self.FindCandidateTiles()
                    
                    #if c1==0 and c2==0:
                    #    print(candidatevalues_in_same_row, candidatevalues_in_same_column, candidatevalues_in_same_box)

            print(self.board)

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

class Solver():
    def __init__(self, board):
        self.board = board
        self.solvingMethods=[]
        self.solvingMethods.append(HiddenSingleMethod(board))
    def Solve(self):
        for i in self.solvingMethods:
            i.Solve()
    def HelperSolve(self):
        for i in self.solvingMethods:
            i.HelperSolve()





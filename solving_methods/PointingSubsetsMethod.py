from  solving_methods.SolvingMethod import SolvingMethod
import math

class PointingSubsetsMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Pointing Subsets Method"
    def Solve(self, helper=False):
        for i in range(9):
            currenttile=self.board.tiles[i][(i*3)%9+math.floor(i/3)]
            currenttile_x=i
            currenttile_y=currenttile.coordinates[1]

            tiles_in_same_row=self.board.tiles[currenttile_x]
            tiles_in_same_column=[k[currenttile_y] for k in self.board.tiles]
            tiles_in_same_box=[g for x,k in enumerate(self.board.tiles) for y,g in enumerate(k) if math.floor(currenttile_x/3)==math.floor(x/3) and math.floor(currenttile_y/3)==math.floor(y/3)]
            
            boxsubsetvalues=self.FindSubset(tiles_in_same_box)
            
            changed=False
            for i in boxsubsetvalues:
                if 1<len(boxsubsetvalues[i])<4:
                    if len(set([j.coordinates[0] for j in boxsubsetvalues[i]]))==1: #if in same row
                        if list(set(boxsubsetvalues[i]) & set(tiles_in_same_row)):
                            for j in [k for k in tiles_in_same_row if k not in tiles_in_same_box]:
                                newvalues="".join([k for k in j.candidatevalues if k!=i])
                                if j.candidatevalues!=newvalues:
                                    changed=True
                                    self.candidateschanged=True
                                    j.candidatevalues=newvalues
                                    j.solecandidate()
                            if changed:
                                return True

                    elif len(set([j.coordinates[1] for j in boxsubsetvalues[i]]))==1: #if in same column
                        if list(set(boxsubsetvalues[i]) & set(tiles_in_same_column)):
                            for j in [k for k in tiles_in_same_column if k not in tiles_in_same_box]:
                                newvalues="".join([k for k in j.candidatevalues if k!=i])
                                if j.candidatevalues!=newvalues:
                                    changed=True
                                    self.candidateschanged=True
                                    j.candidatevalues=newvalues
                                    j.solecandidate()
                            if changed:
                                return True
        return False

    def FindSubset(self, candidatevalueset):
        existingsubsets={str(i+1):[] for i in range(9)}

        for i in candidatevalueset:
            for j in i.candidatevalues:
                existingsubsets[j].append(i)

        return existingsubsets
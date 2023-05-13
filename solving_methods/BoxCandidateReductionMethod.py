from  solving_methods.SolvingMethod import SolvingMethod
import math

class BoxCandidateReductionMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Box Candidate Reduction Method"
        self.description = "A particular digit must appear on a specific row or column within a box. This means that this digit can be eliminated from other rows and columns in the same box"
    def Solve(self, helper=False):
        for i in range(9):
            for j in range(9):
                currenttile=self.board.tiles[i][j]
                currenttile_x=i
                currenttile_y=currenttile.coordinates[1]

                tiles_in_same_row=self.board.tiles[currenttile_x]
                tiles_in_same_column=[k[currenttile_y] for k in self.board.tiles]
                tiles_in_same_box=[g for x,k in enumerate(self.board.tiles) for y,g in enumerate(k) if math.floor(currenttile_x/3)==math.floor(x/3) and math.floor(currenttile_y/3)==math.floor(y/3)]
                
                rowsubsetvalues=self.FindSubset(tiles_in_same_row)
                if self.ReduceFromBox(rowsubsetvalues, tiles_in_same_box):
                    return True

                columnsubsetvalues=self.FindSubset(tiles_in_same_column)
                if self.ReduceFromBox(columnsubsetvalues, tiles_in_same_box):
                    return True

        return False

    def FindSubset(self, candidatevalueset):
        existingsubsets={str(i+1):[] for i in range(9)}

        for i in candidatevalueset:
            for j in i.candidatevalues:
                existingsubsets[j].append(i)

        return existingsubsets

    def ReduceFromBox(self, subsetvalues, box):
        for i in subsetvalues:
            if 1<len(subsetvalues[i])<4:
                tiles_that_are_in_box=[]
                for j in subsetvalues[i]:
                    if j in box:
                        tiles_that_are_in_box.append(j)
                    else:
                        tiles_that_are_in_box=[]
                        break
                if len(tiles_that_are_in_box)>1:
                    changed=False
                    for j in box:
                        if j not in tiles_that_are_in_box:
                            newvalues="".join([k for k in j.candidatevalues if k!=i])
                            if j.candidatevalues!=newvalues:
                                changed=True
                                self.candidateschanged=True
                                j.candidatevalues=newvalues
                                if j.solecandidate():
                                    self.valuefound=True
                    if changed:
                        return True
        return False
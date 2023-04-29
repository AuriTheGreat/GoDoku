import math
import numpy as np
import random
from board import Board

class SolvingMethod():
    def __init__(self, board):
        self.name = "Method"
        self.board = board
        self.candidateschanged=False
        self.valuefound=False
        self.helperresponse=""
    def Solve(self, helper=False):
        return
    def HelperSolve(self, helper=False):
        self.Solve(helper=True)

class CandidateTilesElimination(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Candidate Tiles Elimination"
    def Solve(self, helper=False):
        values=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                if j.value=="":
                    values_in_same_row=[k.value for k in i]
                    values_in_same_column=[k[c2].value for k in self.board.tiles]
                    values_in_same_box=[g.value for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                    newcandidatevalues="".join([t for t in values if t not in values_in_same_row and t not in values_in_same_column and t not in values_in_same_box])
                    j.candidatevalues=newcandidatevalues
                    if len(j.candidatevalues)==1:
                        self.valuefound=True
                        j.value=j.candidatevalues
                        j.candidatevalues=""
                        if helper:
                            self.helperresponse=j.name + " is " + j.value + " because of " + self.name + "." + " The digit is the only possible candidate in the tile."
                            return self.valuefound
                #print([k.value for k in i])
                #print([k[c2].value for k in self.board.tiles])
        return self.valuefound

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

class NakedPairMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Naked Pair Method"
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
                        j.candidatevalues=newvalues
                        if len(j.candidatevalues)==1:
                            self.valuefound=True
                            changed=True
                            j.value=j.candidatevalues[0]
                            j.candidatevalues=""
                if changed:
                    return True
            else:
                existingpairs.append(i.candidatevalues)
        return False

class NakedTripletMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Naked Triplet Method"
    def Solve(self, helper=False):
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
                        for i in candidatevalueset:
                            if i!=a and i!=b and i!=c:
                                newvalues="".join([k for k in i.candidatevalues if k not in sorted(set(a.candidatevalues+b.candidatevalues+c.candidatevalues))])
                                if i.candidatevalues!=newvalues:
                                    self.candidateschanged=True
                                    i.candidatevalues=newvalues
                                    if len(i.candidatevalues)==1:
                                        self.valuefound=True
                                        i.value=i.candidatevalues[0]
                                        i.candidatevalues=""
                        if changed:
                            return True
        return False

class NakedQuadMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Naked Quad Method"
    def Solve(self, helper=False):
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                tiles_in_same_row=i
                if self.FindQuads(tiles_in_same_row):
                    return True

                tiles_in_same_column=[k[c2] for k in self.board.tiles]
                if self.FindQuads(tiles_in_same_column):
                    return True

                tiles_in_same_box=[g for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                if self.FindQuads(tiles_in_same_box):
                    return True
        return False
    def FindQuads(self, candidatevalueset):
        potentialtriplets=[i for i in candidatevalueset if 1<len(i.candidatevalues)<5]
        for c1, a in enumerate(potentialtriplets):
            for c2, b in enumerate(potentialtriplets):
                if c1==c2:
                    continue
                for c3, c in enumerate(potentialtriplets):
                    if c1==c3 or c2==c3:
                        continue
                    for c4,d in  enumerate(potentialtriplets):
                        if c1==c4 or c2==c4 or c3==c4:
                            continue
                        if len(set(a.candidatevalues+b.candidatevalues+c.candidatevalues+d.candidatevalues))==4:
                            changed=False
                            for i in candidatevalueset:
                                if i!=a and i!=b and i!=c and i!=d:
                                    newvalues="".join([k for k in i.candidatevalues if k not in sorted(set(a.candidatevalues+b.candidatevalues+c.candidatevalues+d.candidatevalues))])
                                    if i.candidatevalues!=newvalues:
                                        changed=True
                                        self.candidateschanged=True
                                        i.candidatevalues=newvalues
                                        if len(i.candidatevalues)==1:
                                            self.valuefound=True
                                            i.value=i.candidatevalues[0]
                                            i.candidatevalues=""
                            if changed:
                                return True
        return False

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

class HiddenTripletMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Hidden Triplet Method"
    def Solve(self, helper=False):
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

class PointingPairsMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Pointing Pairs Method"
    def Solve(self, helper=False):
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
    

class Solver():
    def __init__(self, board=""):
        self.solvingMethods=[]
        self.solvingMethods.append(CandidateTilesElimination(board))
        self.solvingMethods.append(HiddenSingleMethod(board))
        self.solvingMethods.append(NakedPairMethod(board))
        self.solvingMethods.append(NakedTripletMethod(board))
        #self.solvingMethods.append(HiddenPairMethod(board))
        #self.solvingMethods.append(HiddenTripletMethod(board))
        self.solvingMethods.append(NakedQuadMethod(board))

        self.board = board
        self.helperresponse=""
        self.solutioncount=0
        if board=="":
            self.GenerateBoard()
    def Solve(self, lastmethod="", helper=False):
        for i in self.solvingMethods:
            if i.name=="Candidate Tiles Elimination" and lastmethod in ["Naked Pair Method", "Naked Triplet Method", "Naked Quad Method", "Hidden Pair Method", "Hidden Triplet Method"]:
                continue
            i.board=self.board
            i.Solve(helper)
            """
            if i.valuefound or i.candidateschanged:
                if i.valuefound:
                    print(i.name, "(Digit found)")
                else:
                    print(i.name, "(Candidates eliminated)")
                print(i.board)
            """
            if i.valuefound:
                i.candidateschanged=False
                i.valuefound=False
                if helper:
                    self.helperresponse=i.helperresponse
                    return True
                self.Solve(helper)
                break
            if i.candidateschanged:
                i.candidateschanged=False
                if helper:
                    self.helperresponse=i.helperresponse
                    return True
                self.Solve(lastmethod=i.name, helper=helper)
                break
        if self.board.isSolved():
            return True
        else:
            return False

    def BruteForceSolve(self):
        def BruteForceSolveSearch(self):
            candidatecountpertile=[len(j.candidatevalues) for i in self.board.tiles for j in i if j.value==""]
            if len(candidatecountpertile)==0:
                puzzlestring=self.board.returnPuzzleString()
                if puzzlestring not in results:
                    results.append(puzzlestring)
                    self.solutioncount+=1
                return
            smallestcandidatecount=min(candidatecountpertile)
            if smallestcandidatecount==0:
                return
            for i in self.board.tiles:
                for j in i:
                    if smallestcandidatecount==len(j.candidatevalues):
                        previousstring=self.board.returnPuzzleString()
                        for k in j.candidatevalues:
                            if self.solutioncount>1:
                                return
                            self.board.insertTiles(previousstring)
                            j.value=k
                            self.Solve()
                            BruteForceSolveSearch(self)


        self.solutioncount=0
        results=[]

        self.Solve()

        BruteForceSolveSearch(self)

        if self.solutioncount==1:
            self.board.insertTiles(results[0])
            return True
        return False


    def HelperSolve(self, helper=False):
        return self.Solve(helper=True)

    def GenerateBoard(self):
        board=[[7, 3, 5, 1, 6, 4, 9, 2, 8],
               [4, 2, 6, 9, 7, 8, 3, 1, 5],
               [1, 9, 8, 5, 3, 2, 6, 7, 4],
               [2, 4, 9, 3, 8, 1, 7, 5, 6],
               [3, 8, 7, 2, 5, 6, 1, 4, 9],
               [5, 6, 1, 7, 4, 9, 8, 3, 2],
               [8, 5, 2, 6, 1, 7, 4, 9, 3],
               [9, 1, 4, 8, 2, 3, 5, 6, 7],
               [6, 7, 3, 4, 9, 5, 2, 8, 1]]


        board=np.matrix(board)

        #shuffles rows and columns within a set of 3 rows and columns
        for i in range(3):
            np.random.shuffle(np.transpose(board)[3*i:3*i+3])
            np.random.shuffle(board[3*i:3*i+3])

        #shuffles the sets of 3 rows around
        newarray=np.array([board[0:3], board[3:6], board[6:9]])
        np.random.shuffle(newarray)
        board=newarray[0]
        board=np.vstack((board, newarray[1], newarray[2]))
        #shuffles the sets of 3 columns around
        board=board.transpose()
        newarray=np.array([board[0:3], board[3:6], board[6:9]])
        np.random.shuffle(newarray)
        board=newarray[0]
        board=np.vstack((board, newarray[1], newarray[2]))
        board=board.transpose()

        #creates board string
        string=""
        for i in range(9):
            for j in range(9):
                string+=str(board[i,j])

        gameboard=Board(string)

        self.board=gameboard

        #removes values from tiles until solver is unable to solve it
        failedattempts=5
        currentattempt=0
        possibletiles=[[i, j] for i in range(9) for j in range(9)]
        lastcorrectpuzzlestring=self.board.returnPuzzleString()
        while currentattempt<failedattempts and possibletiles:
            self.board.insertTiles(lastcorrectpuzzlestring)
            randomcoord=random.choice(possibletiles)
            possibletiles.remove(randomcoord)
            tile=self.board.tiles[randomcoord[0]][randomcoord[1]]
            formervalue=tile.value
            tile.value=""
            puzzlestring=self.board.returnPuzzleString()
            outcome=self.Solve()
            if outcome:
                currentattempt=0
                lastcorrectpuzzlestring=puzzlestring
            else:
                currentattempt+=1
        self.board.insertTiles(lastcorrectpuzzlestring)


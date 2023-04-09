import math
import numpy as np
import random
from board import Board

class SolvingMethod():
    def __init__(self, board):
        self.name = "Method"
        self.board = board
    def Solve(self):
        return
    def HelperSolve(self):
        return

class CandidateTilesElimination(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Candidate Tiles Elimination"
    def Solve(self):
        values=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        outcome=False
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                if j.value=="":
                    values_in_same_row=[k.value for k in i]
                    values_in_same_column=[k[c2].value for k in self.board.tiles]
                    values_in_same_box=[g.value for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                    newcandidatevalues="".join([t for t in values if t not in values_in_same_row and t not in values_in_same_column and t not in values_in_same_box])
                    j.candidatevalues=newcandidatevalues
                    if len(j.candidatevalues)==1:
                        outcome=True
                        j.value=j.candidatevalues
                        j.candidatevalues=""
                #print([k.value for k in i])
                #print([k[c2].value for k in self.board.tiles])
        return outcome

class HiddenSingleMethod(SolvingMethod):
    def __init__(self, board):
        super().__init__(board)
        self.name = "Hidden Single Method"
    def Solve(self):
        for c1, i in enumerate(self.board.tiles):
            for c2, j in enumerate(i):
                candidatevalues_in_same_row=[k.candidatevalues for k in i]
                numbers=self.FindSingles(candidatevalues_in_same_row)
                replacingvalue=[g for g in numbers if g in j.candidatevalues]
                if replacingvalue:
                    j.value=replacingvalue[0]
                    j.candidatevalues=""
                    return True

                candidatevalues_in_same_column=[k[c2].candidatevalues for k in self.board.tiles]
                numbers=self.FindSingles(candidatevalues_in_same_column)
                replacingvalue=[g for g in numbers if g in j.candidatevalues]
                if replacingvalue:
                    j.value=replacingvalue[0]
                    j.candidatevalues=""
                    return True

                candidatevalues_in_same_box=[g.candidatevalues for c3,k in enumerate(self.board.tiles) for c4,g in enumerate(k) if math.floor(c1/3)==math.floor(c3/3) and math.floor(c2/3)==math.floor(c4/3)]
                numbers=self.FindSingles(candidatevalues_in_same_box)
                replacingvalue=[g for g in numbers if g in j.candidatevalues]
                if replacingvalue:
                    j.value=replacingvalue[0]
                    j.candidatevalues=""
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

class Solver():
    def __init__(self, board=""):
        self.solvingMethods=[]
        self.solvingMethods.append(CandidateTilesElimination(board))
        self.solvingMethods.append(HiddenSingleMethod(board))

        self.board = board
        self.solutioncount=0
        if board=="":
            self.GenerateBoard()
    def Solve(self):
        for i in self.solvingMethods:
            i.board=self.board
            outcome=i.Solve()
            if outcome:
                #print(i.name)
                #print(i.board)
                self.Solve()
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


    def HelperSolve(self):
        for i in self.solvingMethods:
            i.HelperSolve()

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


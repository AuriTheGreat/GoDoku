import math
import numpy as np
import random
import time
from board import Board
from solving_methods import CandidateTilesElimination, HiddenSingleMethod, NakedPairMethod, NakedTripletMethod, NakedQuadMethod, HiddenPairMethod, HiddenTripletMethod, PointingSubsetsMethod, BoxCandidateReductionMethod
from solver.Solution import Solution, SolutionStep


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
        self.solvingMethods.append(PointingSubsetsMethod(board))
        self.solvingMethods.append(BoxCandidateReductionMethod(board))

        self.board = board
        self.solutioncount=0


        self.solution=Solution()
        self.helperresponse=""

        if board=="":
            self.GenerateBoard()
    def Solve(self, lastmethod="", helper=False):
        for i in self.solvingMethods:
            if i.name=="Candidate Tiles Elimination" and lastmethod in ["Naked Pair Method", "Naked Triplet Method", "Naked Quad Method", "Hidden Pair Method", "Hidden Triplet Method", "Pointing Subsets Method", "Box Candidate Reduction Method"]:
                continue
            i.board=self.board
            oldboard=self.board.returnPuzzleString_with_candidates()
            i.Solve()
         
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
                    newboard=self.board.returnPuzzleString_with_candidates()
                    self.solution.addsolution(oldboard, newboard, i)
                self.Solve(helper=helper)
                break
            elif i.candidateschanged:
                i.candidateschanged=False
                if helper:
                    newboard=self.board.returnPuzzleString_with_candidates()
                    self.solution.addsolution(oldboard, newboard, i)
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


    def HelperSolve(self, currentboard=""):
        if not self.solution.getsolution(currentboard):
            self.solution=Solution()
            self.board.insertTiles_with_candidates(currentboard)
            if self.Solve():
                self.board.insertTiles_with_candidates(currentboard)
                self.Solve(helper=True)
                self.board.insertTiles_with_candidates(currentboard)
            else:
                return False
        newboard=self.solution.getsolution(currentboard)
        if newboard:
            self.board.insertTiles_with_candidates(newboard)
            self.helperresponse=self.solution.response
            return True
        return False

    def FindCandidates(self):
        CandidateTilesElimination(self.board).Solve()

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
            time.sleep(0.000001) # to ensure there is time to run the main loop while this is running on other thread
            if outcome:
                currentattempt=0
                lastcorrectpuzzlestring=puzzlestring
            else:
                currentattempt+=1
        self.board.insertTiles(lastcorrectpuzzlestring)



class Tile():
    def __init__(self):
        self.value=""
        self.candidatevalues=""
        self.default=False

class Board():
    def __init__(self, string):
        self.tiles = [[Tile() for i in range(9)] for j in range(9)]
        self.insertTiles(string)

    def __str__(self):
        print(("+" + "-"*9)*9 + "+")
        for i in self.tiles:
            for j in i:
                if j.value=="":
                    print("|" + j.candidatevalues.center(9), end="")
                else:
                    print("|" + j.value.center(9), end="")
            print("|")
            print(("+" + "-"*9)*9 + "+")
        return ""

    def isSolved(self):
        puzzlestring=self.returnPuzzleString()
        #check rows
        for i in range(9):
            newvalue="".join(sorted(puzzlestring[i*9:i*9+9]))
            if newvalue!="123456789":
                return False

        #check columns
        for k in range(9):
            newvalue="".join(sorted([i for c, i in enumerate(puzzlestring) if (c+k)%9==0]))
            if newvalue!="123456789":
                return False

        #check boxes
        for k in range(3):
            for g in range(3):
                newvalue="".join(sorted("".join(puzzlestring[k*27+g*9+m*3:k*27+g*9+m*3+3] for m in range(3))))
                if newvalue!="123456789":
                    return False

        return True

    def insertTiles(self, string):
        for c1, i in enumerate(self.tiles):
            for c2, j in enumerate(i):
                newvalue=string[c1*9+c2]
                if newvalue!="0":
                    j.value=newvalue
                    j.default=True

    def returnPuzzleString(self):
        puzzlestring=""
        for i in self.tiles:
            for j in i:
                if len(j.value)==1:
                    puzzlestring+=j.value
                else:
                    puzzlestring+="0"
        return puzzlestring

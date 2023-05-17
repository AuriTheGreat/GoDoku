class Tile():
    def __init__(self, x, y):
        self.coordinates=[x, y]
        self.name="r"+str(x+1)+"c"+str(y+1)
        self.value=""
        self.candidatevalues=""
        self.default=False

    def solecandidate(self):
        if len(self.candidatevalues)==1:
            self.valuefound=True
            changed=True
            self.value=self.candidatevalues[0]
            self.candidatevalues=""
            return True
        return False

class Board():
    def __init__(self, string):
        self.tiles = [[Tile(j, i) for i in range(9)] for j in range(9)]
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
                j.candidatevalues=""
                newvalue=string[c1*9+c2]
                if newvalue!="0":
                    j.value=newvalue
                    j.default=True
                else:
                    j.value=""

    def insertTiles_with_candidates(self, string):
        string=string.split("/")
        for c1, i in enumerate(self.tiles):
            for c2, j in enumerate(i):
                newvalue=string[c1*9+c2]
                if len(newvalue)>1:
                    j.candidatevalues=newvalue
                    j.value=""
                else:
                    j.value=newvalue


    def returnPuzzleString(self):
        puzzlestring=""
        for i in self.tiles:
            for j in i:
                if len(j.value)==1:
                    puzzlestring+=j.value
                else:
                    puzzlestring+="0"
        return puzzlestring

    def returnPuzzleString_with_candidates(self):
        puzzlestring=""
        for c1,i in enumerate(self.tiles):
            for c2,j in enumerate(i):
                puzzlestring+=j.value
                puzzlestring+=j.candidatevalues
                if c1!=8 or c2!=8:
                    puzzlestring+="/"

        return puzzlestring
class Tile():
    def __init__(self):
        self.value=""
        self.default=False

class Board():
    def __init__(self, string):
        self.tiles = [[Tile() for i in range(9)] for j in range(9)]
        self.insertTiles(string)

    def __str__(self):
        print(("+" + "-"*9)*9 + "+")
        for i in self.tiles:
            for j in i:
                print("|" + j.value.center(9), end="")
            print("|")
            print(("+" + "-"*9)*9 + "+")
        return ""

    def isSolved(self):
        pass

    def insertTiles(self, string):
        for c1, i in enumerate(self.tiles):
            for c2, j in enumerate(i):
                newvalue=string[c1*9+c2]
                if newvalue!="0":
                    j.value=newvalue
                    j.default=True
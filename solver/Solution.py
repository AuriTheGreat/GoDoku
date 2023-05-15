import math

class SolutionStep():
    def __init__(self, oldstring, newstring, method):
        self.oldboard=oldstring
        self.newboard=newstring
        self.response=""
        self.skip=False
        oldstring=oldstring.split("/")
        newstring=newstring.split("/")

        differences=[]

        if method.name=="Candidate Tiles Elimination":
            for i in range(81):
                if oldstring[i]!=newstring[i] and len(newstring[i])==1:
                    differences.append(i)

            self.response+=method.name + " has discovered digits: \n"
            if not differences:
                self.skip=True
            for i in differences:
                self.response+=self.gettilecoordinates(i) + ": " + newstring[i] + "\n"
        else:
            for i in range(81):
                if oldstring[i]!=newstring[i]:
                    differences.append(i)

            self.response+=method.name + " made the following changes: \n"
            for i in differences:
                self.response+=self.gettilecoordinates(i) + ": " + oldstring[i] + "->" + newstring[i] + "\n"

        self.response+=method.description + "."

    def gettilecoordinates(self, number):
        return "r" + str(math.floor(number/9)+1) + "c" + str((number%9)+1)

class Solution():
    def __init__(self):
        self.__solutionlist=[]
        self.response=""

    def getsolution(self, currentboard):
        solution=next((x for x in self.__solutionlist if x.oldboard == currentboard), None)
        if solution:
            if solution.skip:
                return self.getsolution(solution.newboard)
            else:
                self.response=solution.response
                return solution.newboard
        else:
            return None

    def addsolution(self, oldboard, newboard, method):
        newsolutionstep=SolutionStep(oldboard, newboard, method)
        self.__solutionlist.append(newsolutionstep)

    def getinitialboard(self):
        if self.__solutionlist:
            return self.__solutionlist[0].oldboard
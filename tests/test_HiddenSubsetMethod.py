import unittest
import board as b
import solver.Solver as s

class HiddenSubsetMethodTest(unittest.TestCase):
    """
    def test1(self):
        #hidden pair
        startingboard="000004028406000005100030600000301000087000140000709000002010003900000507670400000"
        correctanswer="735164928426978315198532674249381756387256149561749832852617493914823567673495281"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    def test2(self):
        #hidden pair
        startingboard="720096003000205000080004020000000060106503807040000000030800090000702000200430018"
        correctanswer="725196483463285971981374526372948165196523847548617239634851792819762354257439618"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    def test3(self):
        #hidden triplet
        startingboard="000001030231090000065003100678924300103050006000136700009360570006019843300000000"
        correctanswer="894571632231698457765243198678924315143857926952136784489362571526719843317485269"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    """

if __name__ == '__main__':
    unittest.main()
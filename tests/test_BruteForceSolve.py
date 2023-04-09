import unittest
import board as b
import solver as s

class BruteForceSolveTest(unittest.TestCase):
    def test1(self):
        #Jellyfish puzzle - way too complicated
        startingboard="024090008800402900719000240075804300240900587038507604082000059007209003490050000"
        correctanswer="624795138853412976719683245975864321246931587138527694382176459567249813491358762"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        self.assertEqual(solver.BruteForceSolve(), True)
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)

    def test2(self):
        #Puzzle with too many solutions
        startingboard="000000520165000070000700800030000000090000000024015008000000003000003167300281040"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        self.assertEqual(solver.BruteForceSolve(), False)

    def test3(self):
        #Puzzle with no solution
        startingboard="056003082000070500300000000000061904014080000005249038000100203001000000002700006"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        self.assertEqual(solver.BruteForceSolve(), False)

    def test4(self):
        #Hidden pairs puzzle
        startingboard="720096003000205000080004020000000060106503807040000000030800090000702000200430018"
        correctanswer="725196483463285971981374526372948165196523847548617239634851792819762354257439618"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        self.assertEqual(solver.BruteForceSolve(), True)
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)

if __name__ == '__main__':
    unittest.main()
import unittest
import board as b
import solver as s

class HiddenSingleMethodTest(unittest.TestCase):
    def test1(self):
        startingboard="000004028406000005100030600000301000087000140000709000002010003900000507670400000"
        correctanswer="735164928426978315198532674249381756387256149561749832852617493914823567673495281"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)

if __name__ == '__main__':
    unittest.main()
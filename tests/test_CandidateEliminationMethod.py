import unittest
import board as b
import solver as s

class CandidateEliminationMethodTest(unittest.TestCase):
    def test1(self):
        startingboard="000000079805074100460100038000658910006917004019432087008206040602000091000500006"
        correctanswer="231865479895374162467129538724658913386917254519432687178296345652743891943581726"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)

    def test2(self):
        startingboard="000105000140000670080002400063070010900000003010090520007200080026000035000409000"
        correctanswer="672145398145983672389762451263574819958621743714398526597236184426817935831459267"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)

if __name__ == '__main__':
    unittest.main()
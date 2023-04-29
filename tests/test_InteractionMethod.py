import unittest
import board as b
import solver as s

class InteractionMethodTest(unittest.TestCase):
    """
    def test1(self):
        #pointing pair
        startingboard="085060001941587263030010085004005816050176000162800500000050040510700000400030059"
        correctanswer="285369471941587263736412985374925816859176324162843597693251748518794632427638159"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    def test2(self):
        #reducing box candidates
        startingboard="400180030030406108081030400269345781140278060008961042894000613000814070010693804"
        correctanswer="456189237732456198981732456269345781145278369378961542894527613623814975517693824"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    """

if __name__ == '__main__':
    unittest.main()
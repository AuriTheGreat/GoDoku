import unittest
import board as b
import solver as s

class NakedSubsetMethodTest(unittest.TestCase):
    def test1(self):
        #naked pair
        startingboard="400000938032094100095300240370609004529001673604703090957008300003900400240030709"
        correctanswer="461572938732894156895316247378629514529481673614753892957248361183967425246135789"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    def test2(self):
        #naked pair
        startingboard="080090030030000000002060108020800500800907006004005070503040900000000010010050020"
        correctanswer="486591732135278469972463158627814593851937246394625871563142987249786315718359624"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    def test3(self):
        #naked triplet
        startingboard="070408029002000004854020007008374200020000000003261700000093612200000403130642070"
        correctanswer="671438529392715864854926137518374296726859341943261785487593612269187453135642978"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)
    def test4(self):
        #naked triplet
        startingboard="294513006600842319300697254000056000040080060000470000730164005900735001400928637"
        correctanswer="294513876675842319318697254129356748547289163863471592732164985986735421451928637"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)

    def test5(self):
        #naked quad
        startingboard="000030086000020040090078520371856294900142375400397618200703859039205467700904132"
        correctanswer="142539786587621943693478521371856294968142375425397618214763859839215467756984132"

        board = b.Board(startingboard)
        solver = s.Solver(board)
        solver.Solve()
        result=board.returnPuzzleString()
        self.assertEqual(result, correctanswer)

if __name__ == '__main__':
    unittest.main()
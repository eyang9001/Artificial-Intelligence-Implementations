import game_manager, game_rules, signal, unittest
from player import makePlayer


class GameTest(unittest.TestCase):


	def makeGame(self, size, player1, player2, depth):
		gm = game_manager.GameManager(
		      size
		    , size
		    , makePlayer(player1, 'x', depth)
		    , makePlayer(player2, 'o', depth)
		    , False)
		signal.signal(signal.SIGABRT, gm.interrupt)
		signal.signal(signal.SIGINT,  gm.interrupt)
		signal.signal(signal.SIGQUIT, gm.interrupt)
		signal.signal(signal.SIGALRM, gm.interrupt)
		return gm


	def test1(self):
		p1 = 'm'
		p2 = 'd'
		depth = 2
		gm = self.makeGame(4, p1, p2, depth)

		# set timeout
		signal.alarm(2)

		gm.play()
		game_rules.printBoard(gm.board)
		print(gm.GetWinner(), "WINS")
		self.assertEqual(gm.board, [['x', ' ', ' ', 'o'], [' ', 'x', ' ', 'x'], [' ', 'o', ' ', 'o'], ['o', 'x', 'o', 'x']])

	def test2(self):
		p1 = 'm'
		p2 = 'd'
		depth = 5
		gm = self.makeGame(4, p1, p2, depth)

		signal.alarm(5)

		gm.play()
		game_rules.printBoard(gm.board)
		print(gm.GetWinner(), "WINS")
		self.assertEqual(gm.board, [['x', ' ', ' ', 'o'], [' ', 'x', ' ', 'x'], [' ', 'o', ' ', 'o'], ['o', 'x', 'o', 'x']])


	def test3(self):
		p1 = 'd'
		p2 = 'm'
		depth = 4
		gm = self.makeGame(6, p1, p2, depth)

		signal.alarm(20)

		gm.play()
		game_rules.printBoard(gm.board)
		print(gm.GetWinner(), "WINS")
		self.assertEqual(gm.board, [[' ', 'o', ' ', 'o', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'x', ' '], ['o', ' ', ' ', 'x', 'o', 'x'], [' ', ' ', 'x', ' ', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x']])

	def test4(self):
		p1 = 'd'
		p2 = 'a'
		depth = 4
		gm = self.makeGame(6, p1, p2, depth)

		signal.alarm(5)

		gm.play()
		game_rules.printBoard(gm.board)
		print(gm.GetWinner(), "WINS")
		print(gm.board)
		self.assertEqual(gm.board, [[' ', 'o', ' ', 'o', ' ', 'o'], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'x', ' '], ['o', ' ', ' ', 'x', 'o', 'x'], [' ', ' ', 'x', ' ', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x']])

	def test5(self):
		p1 = 'a'
		p2 = 'd'
		depth = 6
		gm = self.makeGame(8, p1, p2, depth)

		signal.alarm(300)

		gm.play()
		game_rules.printBoard(gm.board)
		print(gm.GetWinner(), "WINS")
		self.assertEqual(gm.board, [['x', ' ', 'x', ' ', 'x', ' ', ' ', 'o'], [' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'], [' ', ' ', 'x', ' ', 'x', ' ', ' ', 'o'], ['o', ' ', ' ', ' ', ' ', 'x', ' ', 'x'], [' ', 'o', ' ', 'o', ' ', ' ', ' ', 'o'], ['o', ' ', 'o', ' ', ' ', ' ', 'o', 'x'], ['x', ' ', ' ', 'o', ' ', 'o', 'x', 'o'], ['o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']])

if __name__== "__main__":
	unittest.main()

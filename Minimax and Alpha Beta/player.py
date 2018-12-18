import game_rules, random
###########################################################################
# Explanation of the types:
# The board is represented by a row-major 2D list of characters, 0 indexed
# A point is a tuple of (int, int) representing (row, column)
# A move is a tuple of (point, point) representing (origin, destination)
# A jump is a move of length 2
###########################################################################

# I will treat these like constants even though they aren't
# Also, these values obviously are not real infinity, but close enough for this purpose
NEG_INF = -1000000000
POS_INF = 1000000000

class Node(object):
    def __init__(self, board, symbol, depth, move=None):
        self.board = board
        self.children = []
        self.symbol = symbol
        self.depth = depth
        self.move = move
        self.alpha = NEG_INF
        self.beta = POS_INF
    def __str__(self):
        return str(type(self))
    def addChild(self, child):
        self.children.append(child)
    def addVal(self, val):
        self.val=val
    def setAlpha(self, alpha):
        self.alpha = alpha
    def setBeta(self, beta):
        self.beta = beta


class Player(object):
    """ This is the player interface that is consumed by the GameManager. """
    def __init__(self, symbol): self.symbol = symbol # 'x' or 'o'

    def __str__(self): return str(type(self))

    def selectInitialX(self, board): return (0, 0)
    def selectInitialO(self, board): pass

    def getMove(self, board): pass

    def h1(self, board, symbol):
        return -len(game_rules.getLegalMoves(board, 'o' if self.symbol == 'x' else 'x'))


# This class has been replaced with the code for a deterministic player.
class MinimaxPlayer(Player):
    def __init__(self, symbol, depth):
        super(MinimaxPlayer, self).__init__(symbol)
        self.maxDepth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        curdepth = 0
        nextMove = None
        curNode = Node(board, self.symbol, curdepth)
        maxVal = NEG_INF
        for move in legalMoves:
            newboard = game_rules.makeMove(board, move)
            if self.symbol == 'o':
                newChild = self.recursiveX(newboard, curdepth + 1, move)
                curNode.addChild(newChild)
            else:
                newChild = self.recursiveO(newboard, curdepth + 1, move)
                curNode.addChild(newChild)
            if newChild.val > maxVal:
                nextMove = newChild.move
                maxVal = newChild.val
        return nextMove

    def recursiveX(self, board, depth, lastmove):
        legalMoves = game_rules.getLegalMoves(board, 'x')
        newNode = Node(board, 'x', depth, lastmove)
        if depth == self.maxDepth or len(legalMoves) == 0: # terminal node base case here
            newNode.val = self.h1(board, 'x')
            return newNode
        else:  #if there are legal moves for this node
            for move in legalMoves:
                newboard = game_rules.makeMove(board, move)
                newNode.addChild(self.recursiveO(newboard, depth + 1, move))
            if self.symbol == 'x':
                curval = NEG_INF
                for nodes in newNode.children:
                    if nodes.val > curval:
                        curval = nodes.val
            else:
                curval = POS_INF
                for nodes in newNode.children:
                    if nodes.val < curval:
                        curval = nodes.val
            newNode.addVal(curval)
            return newNode

    def recursiveO(self, board, depth, lastmove):
        legalMoves = game_rules.getLegalMoves(board, 'o')
        newNode = Node(board, 'o', depth, lastmove)
        if depth == self.maxDepth or len(legalMoves) == 0:  # terminal node base case here
            h = self.h1(board, 'o')
            newNode.addVal(h)
            return newNode
        else:  # if there are legal moves for this node
            for move in legalMoves:
                newboard = game_rules.makeMove(board, move)
                newNode.addChild(self.recursiveX(newboard, depth + 1, move))
            if self.symbol == 'o':
                curval = NEG_INF
                for nodes in newNode.children:
                    if nodes.val > curval:
                        curval = nodes.val
            else:
                curval = POS_INF
                for nodes in newNode.children:
                    if nodes.val < curval:
                        curval = nodes.val
            newNode.addVal(curval)
            return newNode

# This class has been replaced with the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth):
        super(AlphaBetaPlayer, self).__init__(symbol)
        self.maxDepth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        curdepth = 0
        nextMove = None
        curNode = Node(board, self.symbol, curdepth)
        curNode.setAlpha(NEG_INF)
        curNode.setBeta(POS_INF)
        maxVal = NEG_INF
        for move in legalMoves:
            newboard = game_rules.makeMove(board, move)
            if self.symbol == 'o':
                newChild = self.recursiveX(newboard, curdepth + 1, move, curNode.alpha, curNode.beta)
                curNode.addChild(newChild)
            else:
                newChild = self.recursiveO(newboard, curdepth + 1, move, curNode.alpha, curNode.beta)
                curNode.addChild(newChild)
            if newChild.val > maxVal:
                curNode.addVal(newChild.val)
                maxVal = newChild.val
                nextMove = newChild.move
            if newChild.val > curNode.alpha:
                curNode.setAlpha(newChild.val)

        return nextMove

    def recursiveX(self, board, depth, lastmove, alpha, beta):
        legalMoves = game_rules.getLegalMoves(board, 'x')
        newNode = Node(board, 'x', depth, lastmove)
        newNode.setAlpha(alpha)
        newNode.setBeta(beta)
        if depth == self.maxDepth or len(legalMoves) == 0: # terminal node base case here
            newNode.val = self.h1(board, 'x')
            return newNode
        else:  #if there are legal moves for this node
            if self.symbol == 'x':
                curval = NEG_INF
            else:
                curval = POS_INF
            for move in legalMoves:
                newboard = game_rules.makeMove(board, move)
                newChild = self.recursiveO(newboard, depth + 1, move, newNode.alpha, newNode.beta)
                newNode.addChild(newChild)
                if self.symbol == 'x':
                    if newChild.val > curval:
                        curval = newChild.val
                    if newChild.val > newNode.alpha:
                        newNode.setAlpha(newChild.val)
                    if newChild.val >= newNode.beta:
                        break  # Prunes the nodes here
                else:
                    if newChild.val < curval:
                        curval = newChild.val
                    if newChild.val < newNode.beta:
                        newNode.beta = newChild.val
                    if newChild.val <= newNode.alpha:
                        break #prunes the nodes here
            newNode.addVal(curval)
            return newNode

    def recursiveO(self, board, depth, lastmove, alpha, beta):
        legalMoves = game_rules.getLegalMoves(board, 'o')
        newNode = Node(board, 'o', depth, lastmove)
        newNode.setAlpha(alpha)
        newNode.setBeta(beta)
        if depth == self.maxDepth or len(legalMoves) == 0:  # terminal node base case here
            newNode.addVal(self.h1(board, 'o'))
            return newNode
        else:  # if there are legal moves for this node
            if self.symbol == 'o':
                curval = NEG_INF
            else:
                curval = POS_INF
            for move in legalMoves:
                newboard = game_rules.makeMove(board, move)
                newChild = self.recursiveX(newboard, depth + 1, move, newNode.alpha, newNode.beta)
                newNode.addChild(newChild)
                if self.symbol == 'o':
                    if newChild.val > curval:
                        curval = newChild.val
                    if newChild.val > newNode.alpha:
                        newNode.setAlpha(newChild.val)
                    if newChild.val >= newNode.beta:
                        break  # Prunes the nodes here
                else:
                    if newChild.val < curval:
                        curval = newChild.val
                    if newChild.val < newNode.beta:
                        newNode.beta = newChild.val
                    if newChild.val <= newNode.alpha:
                        break #prunes the nodes here
            newNode.addVal(curval)
            return newNode


class RandomPlayer(Player):
    def __init__(self, symbol):
        super(RandomPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        validMoves = game_rules.getFirstMovesForX(board)
        return random.choice(list(validMoves))

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return random.choice(list(validMoves))

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return random.choice(legalMoves)
        else: return None


class DeterministicPlayer(Player):
    def __init__(self, symbol): super(DeterministicPlayer, self).__init__(symbol)

    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return legalMoves[0]
        else: return None


class HumanPlayer(Player):
    def __init__(self, symbol): super(HumanPlayer, self).__init__(symbol)
    def selectInitialX(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def selectInitialO(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def getMove(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')


def makePlayer(playerType, symbol, depth=1):
    player = playerType[0].lower()
    if player   == 'h': return HumanPlayer(symbol)
    elif player == 'r': return RandomPlayer(symbol)
    elif player == 'm': return MinimaxPlayer(symbol, depth)
    elif player == 'a': return AlphaBetaPlayer(symbol, depth)
    elif player == 'd': return DeterministicPlayer(symbol)
    else: raise NotImplementedException('Unrecognized player type {}'.format(playerType))

def callMoveFunction(player, board):
    if game_rules.isInitialMove(board): return player.selectInitialX(board) if player.symbol == 'x' else player.selectInitialO(board)
    else: return player.getMove(board)



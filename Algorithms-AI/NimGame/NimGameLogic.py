from operator import xor

class Action :
    def __init__(self , row , number):
        self.row = row
        self.number = number
        return


class NimGame :
    def __init__(self , state = [1,3,5,7] , action = Action(0,0)):
        self.state = state
        self.siblings = []
        self.humanTurn = True
        self.action = action
        return

    def printState(self):
        rowNumber = 1
        for row in self.state :
            print "Row Number" , rowNumber , "has" , row , "\t" , "O" * row
            rowNumber += 1
        print ""
        return

    def isEnd (self):
        end = True
        for value in self.state :
            if value != 0 :
                end = False
                break
        return end

    def isLose(self) :
        return self.isLoseState(self.state)

    def isLoseState(self , state):
        sum = 0
        numRows = 0
        for value in state:
            sum += value
            if value > 0:
                numRows = numRows + 1

        if sum == numRows and (sum % 2) == 1:
            return True
        return False

    def isBad(self):
        return self.isBadState(self.state)

    def isBadState(self , state):
        nimSum = 0
        i = 0
        while i < len(state):
            nimSum = xor(nimSum, state[i])
            i = i + 1

        if nimSum == 0:
            return True
        else:
            return False

    def generateSiblings(self):
        self.siblings = []
        rowNumber = 0
        for rowValue in self.state :
            i = 1
            while i <= rowValue :
                tempState = self.state[:]
                tempState[rowNumber] -= i
                action = Action(rowNumber , i)
                self.siblings.append( (NimGame(tempState , action )) )
                i = i + 1
            rowNumber += 1
        return

    def generateSiblingsDepth(self , depth):
        deep = 0
        if deep < depth:
            self.generateSiblings()
            sibling = 0
            while sibling < len(self.siblings) :
                self.siblings[sibling].generateSiblingsDepth(depth - 1)
                sibling = sibling + 1
        return

    def solveWithMiniMax(self , depth = 1 ):
        self.generateSiblingsDepth(depth)
        if self.isBad() :
            bestAction =  self.minimize(depth)
        else:
            bestAction = self.maximize(depth)
        return bestAction.action


    def minimize(self , depth):
        if depth == 0 or self.isEnd():
            return self
        else:
            maxs = []
            for sibling in self.siblings :
                maxs.append( sibling.maximize(depth -1) )
            return self.min(maxs)


    def maximize(self , depth):
        if depth == 0 or self.isEnd():
            return self
        else:
            minis = []
            for sibling in self.siblings :
                minis.append( sibling.minimize(depth -1) )
            return self.max(minis)

    def max(self, states):
        good = []
        bad = []
        for state in states :
            if state.isLose() :
                return state
            elif state.isBad() :
                bad.append(state)
            else:
                good.append(state)

        bestState = NimGame()
        if len(bad) > 0 :
            bestState.action.number = 0
            for state in bad :
                if state.action.number > bestState.action.number :
                    bestState = state
        else:
            bestState.action.number = 100
            for state in good:
                if state.action.number < bestState.action.number:
                    bestState = state
        return bestState

    def min(self , states):
        good = []
        bad = []
        for state in states :
            if not state.isBad() and not state.isLose() :
                return state
            elif not state.isBad() :
                good.append(state)
            else:
                bad.append(state)

        bestState = NimGame()
        if len(good) > 0 :
            bestState.action.number = 100
            for state in good :
                if state.action.number < bestState.action.number :
                    bestState = state
                else:
                    bestState.action.number = 0
                    for state in bad:
                        if state.action.number > bestState.action.number:
                            bestState = state
        return bestState


game = NimGame()

while not game.isEnd() :
    if game.humanTurn :
        while True :
            game.printState()
            print "This is your Turn "
            print "\tYou must take some Balls ..."
            row = input('Please enter number of row : ')
            number = input('Please enter number of Balls : ')
            if row > 0 and row < len(game.state) + 1 :
                if number > 0 and number <= game.state[row - 1] :
                    break
        game.state[row - 1] -= number
        game.humanTurn = False
    else:
        print "This is Computer Turn "
        action = game.solveWithMiniMax()
        print "Computer take" , action.number , "from row" , action.row + 1
        game.state[action.row] -= action.number
        game.humanTurn = True

print "\n"
print "Thanks for The game"
if game.humanTurn :
    print "You are the winner :'D"
else:
    print "Computer beat You lol"
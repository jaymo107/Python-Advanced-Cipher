import random

class Cipher:
    __grid = []
    __cols = 6
    __rows = 6
    __gridSize = __cols * __rows
    __secretWord = None
    __characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __sequence = []
    __xLabel = ["A", "B", "C", "D", "E", "F"]
    __yLabel = ["A", "B", "C", "D", "E", "F"]

    def setWord(self, word):
        self.__secretWord = word

    def getWord(self):
        return self.__secretWord

    """
    Generate a random character that hasn't appeared before already
    """
    def randomizeGrid(self):
        return random.sample(range(0, self.__gridSize), self.__gridSize)

    """
    Generate a grid to a given size and give it random characters
    """
    def generateGrid(self):

        characters = self.randomizeGrid()
        printed = ""
        for i in range(0, self.__gridSize):
            self.__grid.append(self.__characters[characters[i]])
            printed += self.__grid[i]

    """
    get letter at given x and y coordinates
    """
    def getLetterAt(self, x, y):
        return self.__grid[x + self.__cols*y]

    def getX(self, i):
        return i % self.__cols

    def getY(self, i):
        return i / self.__rows
    """
    Encode the inputted string using the encoder and print to the screen
    """
    def encode(self, string):
        string = string.upper()
        encoded = ""
        for i in range(0, len(string)):
            if string[i] == " ":
                encoded += " "
                continue

            index = self.__grid.index(string[i])

            encoded += self.__xLabel[self.getX(index)]+self.__xLabel[self.getY(index)]+" "
        return encoded

    """
    format and print the grid to the user
    """
    def printGrid(self):
        for i in range(0, self.__gridSize):
            x = self.getX(i)
            y = self.getY(i)
            print "%i. %s at location (%s, %s) is encoded to [%s]" % (i, self.__grid[i], x, y, self.encode(self.getLetterAt(x,y)))

    """
    decode the string back to the original string
    """
    def decode(self):
        pass

    def __init__(self):
        self.__secretWord = "lol"
        self.generateGrid()

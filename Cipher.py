import random
import re

class Cipher:
    __lowerGrid = []
    __upperGrid = []
    __finalGrid = []
    __cols = 6
    __rows = 6
    __gridSize = __cols * __rows
    __secretWord = ""
    __upperCharacters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __lowerCharacters = "0123456789abcdefghijklmnopqrstuvwxyz"
    __sequence = []
    __lowerXlabel = ["A", "B", "C", "D", "E", "F"]
    __lowerYlabel = ["A", "B", "C", "D", "E", "F"]
    __encodedWord = None
    __originalString = None

    def setWord(self):
        self.__secretWord = ""
        while len(self.__secretWord) <= 0 or len(self.__originalString) % len(self.__secretWord) != 0:
            print "Set a secret word divisible by the original string: "
            self.__secretWord = raw_input("\n")

        print "Secret word set successfully"

    def getWord(self):
        return self.__secretWord

    """
    Generate a random character that hasn't appeared before already
    """
    def randomizeGrid(self):
        return random.sample(range(0, self.__gridSize), self.__gridSize)

    """
    Generate the grids (upper case and lower case) to a given size and give them random characters
    """
    def generateGrids(self):

        lower = self.randomizeGrid()
        for i in range(0, self.__gridSize):
            self.__lowerGrid.append(self.__lowerCharacters[lower[i]])

        upper = self.randomizeGrid()
        for i in range(0, self.__gridSize):
            self.__upperGrid.append(self.__upperCharacters[upper[i]])

    """
    get letter at given x and y coordinates
    """
    def getLetterAt(self, x, y):
        return self.__lowerGrid[x + self.__cols * y]

    def getX(self, i):
        return i % self.__cols

    def getY(self, i):
        return i / self.__rows
    """
    Encode the inputted string using the encoder and print to the screen
    """
    def encode(self, string):
        encoded = ""

        self.__originalString = string

        """
        remove non alphanumeric characters
        """
        pattern = re.compile('([^\s\w]|_)+')
        string = re.sub(pattern, '', string)

        for i in range(0, len(string)):

            if string[i] == " ":
                encoded += " "
                continue

            if string[i].islower():
                index = self.__lowerGrid.index(string[i])
            else:
                index = self.__upperGrid.index(string[i])

            encoded += self.__lowerXlabel[self.getX(index)] + self.__lowerXlabel[self.getY(index)] + " "

        self.__encodedWord = encoded
        self.setWord()
        return encoded

    """
    format and print the grid to the user
    """
    def printGrid(self):
        for i in range(0, self.__gridSize):
            x = self.getX(i)
            y = self.getY(i)
            print "%i. %s at location (%s, %s) is encoded to [%s]" % (i, self.__lowerGrid[i], x, y, self.encode(self.getLetterAt(x, y)))

    """
    decode the string back to the original string
    """
    def decode(self, string):
        decoded = ""

        if self.getWord() is None:
            return "You need to set a secret word"

        """
        split the string into the coded letter combinations
        """
        codes = string.split(' ')

        for i in range(0, len(codes)):
            if codes[i] == " ":
                decoded += " "
                continue
            try:
                xPos = self.__lowerXlabel.index(codes[i][0])
                yPos = self.__lowerYlabel.index(codes[i][1])
                decoded += self.getLetterAt(xPos, yPos)
            except IndexError:
                decoded += " "

        return decoded

    def __init__(self):
        self.generateGrids()

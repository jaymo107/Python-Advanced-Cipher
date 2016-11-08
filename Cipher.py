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
    __lowerCharacters = __upperCharacters.lower()
    __sequence = []
    __lowerXlabel = ["A", "B", "C", "D", "E", "F"]
    __lowerYlabel = ["A", "B", "C", "D", "E", "F"]
    __encodedWord = None
    __originalString = None

    """
    Set the secret word in the application
    """
    def setWord(self, word):
        if len(self.__originalString) % len(word) != 0:
            print "Word must be divisible by original string: "
            word = raw_input("\n")
            """
            Call this function recursively
            """
            self.setWord(word)
        self.__secretWord = word
        self.generateGrids(word)
        return "Secret word set"

    """
    Return the secret word
    """
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
    def generateGrids(self, keyword=None):

        if keyword:
            codes = self.__encodedWord.split(' ')

            for i in range(0, len(codes)):
                self.__finalGrid.append(codes[i])

        else:
            lower = self.randomizeGrid()
            for i in range(0, self.__gridSize):
                self.__lowerGrid.append(self.__lowerCharacters[lower[i]])

            upper = self.randomizeGrid()
            for i in range(0, self.__gridSize):
                self.__upperGrid.append(self.__upperCharacters[upper[i]])

    """
    get letter at given x and y coordinates
    """
    def getLetterAt(self, x, y, grid="lower"):
        if grid == "lower":
            return self.__lowerGrid[x + self.__cols * y]
        elif grid == "upper":
            return self.__upperGrid[x + self.__cols * y]
        elif grid == "final":
            return self.__finalGrid[x + len(self.getWord()) * y]

    """
    Return the X value based ona row/column structure
    """
    def getX(self, i, grid = None):
        return i % self.__cols

    """
    Return the Y value based ona row/column structure
    """
    def getY(self, i, grid = None):
        return i / self.__rows

    """
    Encode the inputted string using the encoder and print to the screen
    """
    def encode(self, string):
        encoded = ""

        """
        remove non alphanumeric characters
        """
        pattern = re.compile(r'\W+')
        string = re.sub(pattern, '', string)

        self.__originalString = string

        for i in range(0, len(string)):

            if string[i] == " ":
                encoded += ""
                continue

            if string[i].islower():
                index = self.__lowerGrid.index(string[i])
            else:
                index = self.__upperGrid.index(string[i])

            encoded += self.__lowerXlabel[self.getX(index)] + self.__lowerXlabel[self.getY(index)] + " "

        self.__encodedWord = encoded
        return self.__encodedWord

    """
    format and print the grid to the user
    """
    def printGrid(self):
        lowerPrinter = "Lowercase Grid: \n\t"

        for i in range(0, len(self.__lowerGrid)):
            x = self.getX(i)
            y = self.getY(i)

            if x < self.__cols - 1:
                lowerPrinter += self.encode(self.getLetterAt(x, y, "lower"))
            else:
                lowerPrinter += "\n\t"

        upperPrinter = "Uppercase Grid: \n\t"

        for i in range(0, len(self.__upperGrid)):
            x = self.getX(i)
            y = self.getY(i)

            if x < self.__cols - 1:
                upperPrinter += self.encode(self.getLetterAt(x, y, "upper"))
            else:
                upperPrinter += "\n\t"

        final = "Secret Grid: \n\t"
        counter = 0

        for i in range(0, len(self.__finalGrid)):
            final += self.__finalGrid[i]+" "


        print lowerPrinter + "\n\n" + upperPrinter + "\n\n" + final

    """
    decode the string back to the original string
    """
    def decode(self, string):
        decoded = ""

        if len(self.getWord()) <= 0:
            return "You need to set a secret word"

        """
        split the string into the coded letter combinations
        """
        codes = string.split(' ')

        for i in range(0, len(codes)):
            if codes[i] == " ":
                decoded += ""
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
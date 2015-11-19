import random
import string
import sys

class Cipher:

    __grid = [[]]
    __gridSize = 8
    __secretWord = ""

    def setWord(self, word):
        self.__secretWord = word

    def getWord(self):
        return __secretWord

    def setGridSize(self, size):
        self.__gridSize = size

    def getGridSize(self):
        return __gridSize

    def randomChar(self):
        return chr(random.randrange(97, 97 + 26))

    def generateGrid(self):
        self.__grid = [[0 for i in xrange(self.__gridSize)] for i in xrange(self.__gridSize)]

        for x in range(len(self.__grid)):
            for y in range(len(self.__grid[x])):
                self.__grid[x][y] = self.randomChar()

    #format and print the grid to the user
    def printGrid(self):
        for x in range(len(self.__grid)):
            sys.stdout.write(self.__grid[x][0]+"\n")

            for y in range(len(self.__grid)):
                sys.stdout.write(self.__grid[x][y])

    #Encode the inputted string using the encoder and print to the screen
    def encode():
        pass

    #decode the string back to the original string
    def decode():
        pass

    def __init__(self, size, word):
        self.__gridSize = size
        self.__secretWord = word
        self.generateGrid()

cipher = Cipher(8, 'omg')
cipher.printGrid()

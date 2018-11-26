import sys,os
import sudoku_validate
import random

def main():

    def generateSudoku():
        sudoku = []
        tries = 0
        orderedRow = [i for i in range(1,10)]

        for row in range(1,10):
            shuffledRow = random.sample(orderedRow, len(orderedRow))
            sudoku.extend(shuffledRow)
        while sudoku_validate.bruteValidate(sudoku) == False:
            sudoku = []
            orderedRow = [i for i in range(1,10)]
            for row in range(1,10):
                shuffledRow = random.sample(orderedRow, len(orderedRow))
                sudoku.extend(shuffledRow)

            tries+=1
            print (" #", tries)
        return sudoku

    generatedSudoku = generateSudoku()
    sudoku_validate.bruteValidate(generatedSudoku)
    sudoku_validate.printSudoku(generatedSudoku)

if __name__ == "__main__":
    main()

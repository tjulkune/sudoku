import sys,os
import sudoku_validate
import random

def main():
    # generate single valid sudoku block
    def generateBlock():
        generatedBlock = []
        tries = 0
        orderedPartBlock = [i for i in range(1,10)]
        for row in range(1,4):
            shuffledPartBlock = []

            step = 3
            blockNum = 0
            blockSeek = 0
            blockPos = 0
            invalidPart = True

            #generate blocks until valid block is found
            while (invalidPart == True):
                sudoku = []
                tries+=1
                print (" #", tries)
                orderedPartBlock = [i for i in range(1,10)]

                #generate 3 rows for block calculation
                for row in range(1,4):
                    shuffledRow = random.sample(orderedPartBlock, len(orderedPartBlock))
                    sudoku.extend(shuffledRow)

                for iter in range(0,3,step):
                    blockPos = iter
                    subRow1 = sudoku[(blockPos):(blockPos)+step]
                    subRow2 = sudoku[(blockPos)+9:(blockPos)+step+9]
                    subRow3 = sudoku[(blockPos)+18:(blockPos)+step+18]
                    print("subRow1: ",subRow1)
                    print("subRow2: ", subRow2)
                    print("subRow3: ", subRow3)

                    partBlock = []

                    partBlock.extend(subRow1)
                    partBlock.extend(subRow2)

                    # check first 2 rows for duplicates
                    if (len(partBlock) != len(set(partBlock))):
                        print ("Invalid partial sudokublock: ",partBlock)
                        invalidPart = True
                    # check last row against earlier ones
                    else:
                        fullBlock = []
                        fullBlock = partBlock
                        fullBlock.extend(subRow3)
                        if (sudoku_validate.checkDuplicates(fullBlock) == False):
                            print ("Invalid full sudokublock: ",fullBlock)
                            invalidPart = True
                        else:
                            print ("Valid full sudokublock: ",fullBlock)
                            invalidPart = False


            generatedBlock = fullBlock
                    # jump to next row of block
                    # if (iter % 9 == 0 and iter != 0):
                    #     blockSeek += 18
                    # else:
                    #     blockSeek += 0
                    #print ("iter ", iter, "+ blockSeek", blockSeek, "= ", iter+blockSeek)

            return generatedBlock

    # def generateSudoku():
    #      generatedSudoku = []
    #      for block in range(1,10):
    #          singleBlock = generateBlock()
    #          orderedPartBlockRow = [i for i in range(1,10)]
    #          shuffledPartBlockRow = random.sample(orderedPartBlockRow, len(orderedPartBlock))
    #          duplicateRowNumbers = True
    #          while(duplicateRowNumbers == True)
    #             for num in range(1,4):
    # #                 if sudoku_validate.checkDuplicates == True:
    #
    #          generatedSudoku.extend(singleBlock)
    #          if generatedSudoku
    #      return generatedSudoku

    doku = generateBlock()
    print("Sudoku Block Generation complete")
    #sudoku_validate.bruteValidate(generatedSudoku)
    sudoku_validate.printSudoku(doku)

if __name__ == "__main__":
    main()

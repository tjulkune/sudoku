import sys, os

def printSudoku(sudoku):
    for index, number in enumerate(sudoku):
        if((index+1) % 27 == 0 and index!=0):
                print(number, end='\n\n')
        elif((index+1) % 9 == 0 and index!=0):
                    print(number, end='\n')
        elif((index+1) % 3 == 0):
            print (number, end='  ')
        elif((index+1) % 3 == 0):
            print (number, end='')
        else:
            print(number, end='')

# get sudoku blocks from list and check if valid
# we simpply iterate through the list and jump to correct cell with addition
def validateBlocks(sudoku):
    print("Validating blocks")
    validBlocks = True
    step = 3
    blockNum = 0
    blockSeek = 0
    blockPos = 0
    for iter in range(0,27,step):
        # jump to next row of blocks
        if (iter % 9 == 0 and iter != 0):
            blockSeek += 18
        else:
            blockSeek += 0
        #print ("iter ", iter, "+ blockSeek", blockSeek, "= ", iter+blockSeek)
        blockPos = iter + blockSeek
        subRow1 = sudoku[(blockPos):(blockPos)+step]
        subRow2 = sudoku[(blockPos)+9:(blockPos)+step+9]
        subRow3 = sudoku[(blockPos)+18:(blockPos)+step+18]
        print("subRow1: ",subRow1)
        print("subRow2: ", subRow2)
        print("subRow3: ", subRow3)

        fullBlock = []
        fullBlock.extend(subRow1)
        fullBlock.extend(subRow2)
        fullBlock.extend(subRow3)
        #print ("fullblock:" , fullBlock)
        if (checkDuplicates(fullBlock, 9) == True):
            print ("Valid block: ",fullBlock)
        else:
            print ("Invalid block: ",fullBlock)
            validBlocks = False
        blockNum+=1

    print("found", blockNum, " blocks")
    return validBlocks

def validateRows(sudoku):
    validRows = True
    print("Validating rows")
    for val in range(0,len(sudoku),9):
        row = sudoku[val:val+9]
        #print ("row: ", row)
        if (checkDuplicates(row, 9) == True):
            print ("Valid row: ", row)
        else:
            print ("Invalid row: ",row)
            validRows = False
    return validRows

def validateColumns(sudoku):
    print("Validating columns")
    step = 9
    col = []
    validColumns = True
    for val in range(0, 9, 1):
        col=[sudoku[val]]
        #print("val", val)
        for num in range(val, len(sudoku)-9, step):
            col.append(sudoku[num+9])
            #print(col)
        if (checkDuplicates(col, 9) == True):
            print ("Valid column: ", col)
        else:
            validColumns = False
            print ("Invalid column: ", col)
    return validColumns



def bruteValidate(sudoku):
    validRows = validateRows(sudoku)
    validBlocks = validateBlocks(sudoku)
    validColumns = validateColumns(sudoku)
    validSolution = False
    if (validRows == True and validBlocks == True and validColumns  == True):
        validSolution = True
    print ("rows: ", validRows, " blocks: ", validBlocks, " columns: ", validColumns)
    return validSolution

# chunk is range of numbers to check
# e.g 3 for first row of a single block
# 9 for full block, row or column
def checkDuplicates(sudokuPart, chunk):
    validArea = True
    area = sudokuPart
    print ("Validating area: ",area)
    for checkval in range(1,chunk+1):
      if area.count(checkval) == 1:
         print("1 occurrence of", checkval, "found")
      elif area.count(checkval) != 0:
         print("Multiple occurrences of", checkval, "invalid area!")
         validArea = False
      elif area.count(checkval) == 0:
         print("No occurrences of", checkval, "invalid area!")
         validArea = False
    return validArea

def main():
    invalidSolvedSudoku = [
        1,2,3,4,5,6,7,8,9,
        2,3,4,5,6,7,8,9,1,
        3,4,4,6,7,8,9,1,2,

        4,5,6,7,8,9,1,2,3,
        5,6,7,8,9,1,2,3,4,
        6,7,8,9,1,2,3,4,5,

        7,8,9,1,2,3,4,5,6,
        8,9,1,2,3,4,5,6,7,
        9,1,2,3,4,5,6,7,8]

    validSolvedSudoku = [
        7,3,5,6,1,4,8,9,2,
        8,4,2,9,7,3,5,6,1,
        9,6,1,2,8,5,3,7,4,

        2,8,6,3,4,9,1,5,7,
        4,1,3,8,5,7,9,2,6,
        5,7,9,1,2,6,4,3,8,

        1,5,7,4,9,2,6,8,3,
        6,9,4,7,3,8,2,1,5,
        3,2,8,5,6,1,7,4,9
    ]

    if (bruteValidate(validSolvedSudoku) == False):
        print('Invalid sudoku solution')
    else:
        print('Congrats, sudoku solution is valid')
    printSudoku(validSolvedSudoku)

if __name__ == "__main__":
    main()

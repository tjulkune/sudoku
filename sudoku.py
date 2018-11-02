sudoku1 = [
    1,2,3,4,5,6,7,8,9,
    2,3,4,5,6,7,8,9,1,
    3,4,4,6,7,8,9,1,2,

    4,5,6,7,8,9,1,2,3,
    5,6,7,8,9,1,2,3,4,
    6,7,8,9,1,2,3,4,5,

    7,8,9,1,2,3,4,5,6,
    8,9,1,2,3,4,5,6,7,
    9,1,2,3,4,5,6,7,8]

# fancy printing, broken atm
def printSudoku(sudoku):
    for val in range(0,81):
        for index, number in enumerate(sudoku):
            if((index+1) % 3 == 0):
                print (number)
            elif((index+1) % 9 == 0 and index!=0):
                print(number, 'sttt\n')
            else:
                print(number, end='')

# get sudoku blocks from list and check if valid
def solveBlocks(sudoku):
    start = 0
    step = 3
    for val in range(start,len(sudoku)-18,step):
       block = [sudoku[val:val+step]]
       block.append(sudoku[val+9:val+step+9])
       block.append(sudoku[val+18:val+step+18])
       if (checkDuplicates(block) == True):
           print ("valid block: ",block)
       else:
           print ("invalid block: ",block)

def solveRows(sudoku):
    for val in range(0,len(sudoku),9):
       row = sudoku[val:val+9]
       #print ("row: ", row)
       if (checkDuplicates(row) == True):
           print ("valid row: ", row)
       else:
           print ("invalid row: ",row)


def bruteSolve(sudoku):
    validRows = solveRows(sudoku)
    validBlocks = solveBlocks(sudoku)
    validColumns = True
    validSolution = False
    if (validRows and validBlocks  == True):
        validSolution = True
    return validSolution

def checkDuplicates(sudokuPart):
    validArea = True
    area = sudokuPart
    print ("checking area: ",area)
    for checkval in range(1,10):
      if area.count(checkval) == 1:
         print("1 occurrence of", checkval, "found")
      elif area.count(checkval) != 0:
         print("multiple occurrences of", checkval, "invalid area!")
         validArea = False
      elif area.count(checkval) == 0:
         print("no occurrences of", checkval, "invalid area!")
         validArea = False
    return validArea
#print_sudoku(sudoku1)
#solveBlocks(sudoku1)
if (bruteSolve(sudoku1) == False):
    print('Invalid sudoku solution')
else:
    print('Congrats, sudoku solution is valid')

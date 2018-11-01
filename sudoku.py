sudoku1 = [
    1,2,3,4,5,6,7,8,9,
    2,3,4,5,6,7,8,9,1,
    3,4,4,6,7,8,9,1,2,

    4,5,6,7,8,9,1,2,3,
    5,6,7,8,9,1,2,3,4,
    6,7,8,9,1,2,3,4,5,

    7,8,9,1,2,3,4,5,6,
    8,9,1,2,3,4,5,6,7,
    9,1,2,3,4,5,6,7,8
]

#print(sudoku1)
def print_sudoku(sudoku):
    for index, number in enumerate(sudoku):
        if((index+1) % 3 == 0):
            print (number)
        elif((index+1) % 9 == 0 and index!=0):
            print(number, 'sttt\n')
        else:
            print(number, end='')

def brute_solve(sudoku):
    validSolution = True
    for val in range(0,81,9):
       print(val)
       row = sudoku[val:val+9]
       print(row)
       for checkval in range(1,10):
         if row.count(checkval) == 1:
            print("1 occurrence of", checkval, "found")
         elif row.count(checkval) != 0:
            print("multiple occurrences of", checkval, "invalid block!")
            validSolution = False
         elif row.count(checkval) == 0:
            print("no occurrences of", checkval, "invalid block!")
            validSolution = False
    return validSolution
print_sudoku(sudoku1)
if (brute_solve(sudoku1) == False):
    print('Invalid sudoku solution')
else:
    print('Congrats, sudoku solution is valid')

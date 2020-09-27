import time
import numpy as np

#edit puzzle and order to solve different puzzles
puzzle = [[2,0,0,12,14,0,0,10,0,0,0,9,0,13,1,0],
[13,15,16,0,0,0,0,0,4,0,0,6,12,0,0,9],
[0,8,0,6,0,0,0,0,0,7,14,0,0,0,2,11],
[0,0,1,4,13,8,6,9,0,0,11,0,16,0,0,7],
[0,1,2,15,0,14,0,0,0,0,0,3,0,0,0,0],
[3,10,0,8,0,0,0,5,14,16,0,7,2,12,0,1],
[12,11,0,0,0,0,8,0,0,5,2,0,0,0,4,16],
[0,9,7,0,0,0,3,2,6,12,13,11,5,0,0,0],
[1,0,0,0,6,0,5,0,0,14,0,0,0,0,0,0],
[8,0,0,2,3,0,0,11,0,0,0,0,0,0,13,14],
[0,6,15,7,10,0,0,14,12,0,0,1,0,0,16,5],
[0,0,14,10,0,9,15,0,5,0,0,0,3,11,0,2],
[0,13,0,0,0,0,14,6,0,11,12,0,15,16,0,0],
[0,0,0,0,11,0,0,16,0,0,10,8,4,1,0,0],
[0,4,10,3,5,13,12,15,0,1,16,0,0,0,0,0],
[0,0,0,11,2,4,0,0,3,9,15,0,0,0,12,6]]
order = (4,4)

class sudoku:
    solutions = 0

    def print_array(array, order):   #prints board
        d, r_sb, c_sb = order[0] * order[1], order[0], order[1]
        for x in range(d):
                for y in range(d):
                    if (y + 1) % c_sb == 0 and y+1 != d:
                        print(f"{array[x][y]:3d}", end=" |")
                    else:
                        print(f"{array[x][y]:3d}", end="")
                print()
                if (x + 1) % r_sb == 0 and (x+1) != d:
                    print("-" * ((3 * order[0] * order[1]) + order[0] * 2 ))
        print()

    def possible_values(array, order):      #possible values for all zero elements
        r, c, d = order[0], order[1], order[0]*order[1]
        values = []
        for i in range(d):
            for j in range(d):
                if array[i][j] == 0:
                    impossible_values = list(set(array[i]+ np.array(array).transpose()[j].tolist()+[array[k][l] for k in range(i-i%r, i - i%r + r) for l in range(j-j%c,j-j%c+c) if array[k][l]!= 0]))
                    possible_values = [k for k in np.arange(1, d+1) if k not in impossible_values]
                    possible_values.insert(0,(i,j))
                    values.append(possible_values)
        values.sort(key=len)      #puts the solutions that are more certain at front to optimize backpropagation
        return values

    def possible(array, row, col, order,num):        #checks if a value(num) is valid in given position(row, col) in sudoku(array) of dimension(order)
        d, r, c = order[0]*order[1], order[0], order[1]
        for i in range(0,d):        #checks possibility in rows and columns
            if array[row][i] == num or array[i][col] == num:
                return False
        row0, col0= (row//r)*r, (col//c)*c      #this block of code checks possibility in boxes
        for i in range(0, r):         #THIS CAN BE EDITED AND SHORTENED
            for j in range(0, c):
                if array[row0+i][col0+j] == num:
                    return False
        return True

    
    def solve(array, order, print_):        # solves puzzle and returns number of solutions
        def solver(array, order, print_):      
            d, r, c = order[0]*order[1], order[0], order[1]
            values = sudoku.possible_values(array, order)
            for i in range(len(values)):
                for value in values:
                    for num in range(1, len(value)):
                        row, col = value[0][0], value[0][1]
                        if sudoku.possible(array, row, col, (r, c) ,value[num]):
                            array[row][col] = value[num]
                            solver(array, order,print_)
                            array[row][col] = 0
                    return
            if print_ == 1: sudoku.print_array(array, order)
            sudoku.solutions += 1
        solver(array, order, print_)
        return sudoku.solutions

sudoku.print_array(puzzle, order)
start_time = time.time()
print("\n"+"Solving..."+"\n")
print("\n"+"Number of solutions:     "+ str(sudoku.solve(puzzle, order, 1)))
print("\n"+"Solved in ", (time.time() - start_time), " seconds."+"\n")

# manualinput and example problems
puzzle1 = [[0, 0, 0, 0, 3, 0, 0, 0, 5], [0, 4, 0, 6, 0, 9, 3, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 8],
           [7, 9, 0, 0, 0, 1, 6, 0, 3], [0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 3, 0, 9, 4, 6, 7, 0, 0],
           [3, 6, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 0, 2, 9], [0, 0, 8, 0, 0, 4, 0, 0, 0]]
order1 = (9, 3, 3) # (dimension, row of subsize, column of subsize... 3 row and 3 column make one box)

order2 = (12, 3, 4)  # (dimension, row of subsize, column of subsize... 3 row and 4 column make one box)
puzzle2 = [[0, 0, 10, 0, 0, 0, 6, 0, 0, 0, 0, 9],
           [0, 4, 0, 6, 2, 0, 0, 11, 0, 0, 0, 10],
           [0, 0, 0, 1, 0, 4, 0, 0, 0, 7, 0, 3],
           [0, 0, 8, 0, 0, 0, 11, 1, 0, 3, 7, 12],
           [1, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 5],
           [0, 12, 0, 0, 5, 2, 0, 7, 4, 6, 0, 0],
           [0, 0, 5, 4, 11, 0, 9, 2, 0, 0, 1, 0],
           [9, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 11],
           [7, 8, 12, 0, 3, 1, 0, 0, 0, 9, 0, 0],
           [8, 0, 11, 0, 0, 0, 3, 0, 5, 0, 0, 0],
           [2, 0, 0, 0, 10, 0, 0, 4, 9, 0, 12, 0],
           [6, 0, 0, 0, 0, 12, 0, 0, 0, 11, 0, 0]]

def print_array(array, order):   # prints solved board
    for x in range(order[0]):
            for y in range(order[0]):
                if (y + 1) % order[2] == 0 and y != 0:
                    print(f"{array[x][y]:3d}", end=" |")
                else:
                    print(f"{array[x][y]:3d}", end="")
            print()
            if (x + 1) % order[1] == 0 and x != 0:
                print("-" * ((3 * order[1] * order[2]) + order[1] * 2))

def possible(array, row,col, order,num):        # checks if a value is valid in the given position
    d, r_sb, c_sb = order[0], order[1], order[2]
    for i in range(0,d):
        if array[row][i] == num:
            return False
    for i in range(0,d):
        if array[i][col] == num:
            return False
    col0 = (col//c_sb)*c_sb 
    row0 = (row//r_sb)*r_sb
    for i in range(0,r_sb):
        for j in range(0,c_sb):
            if array[row0+i][col0+j] == num:
                return False
    return True

def solve(array, order):            # recursive function
    d = order[0]
    for row in range(d):  
        for col in range(d):
            if array[row][col] == 0:
                for num in range(1, d+1):
                    if possible(array, row,col,order,num):
                        array[row][col] = num
                        solve(array, order)
                        array[row][col] = 0
                return 
    print_array(array, order)
    

solve(puzzle1, order1)
solve(puzzle2, order2)

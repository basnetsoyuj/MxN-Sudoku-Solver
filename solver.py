import copy

# input the sudoku puzzle
# order = (m,n)  m rows and n columns make 1 box
puzzle1 = [[0, 0, 0, 0, 3, 0, 0, 0, 5], [0, 4, 0, 6, 0, 9, 3, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 8],
           [7, 9, 0, 0, 0, 1, 6, 0, 3], [0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 3, 0, 9, 4, 6, 7, 0, 0],
           [3, 6, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 0, 2, 9], [0, 0, 8, 0, 0, 4, 0, 0, 0]]
order1 = (3, 3)

order2 = (3, 4)  # 3 rows and 4 columns make 1 box
puzzle2 = [[0, 0, 0, 2, 1, 11, 5, 0, 8, 10, 0, 0], [9, 0, 8, 0, 2, 0, 10, 0, 0, 3, 5, 7],
           [10, 0, 0, 6, 4, 0, 0, 9, 11, 0, 12, 0], [0, 12, 0, 3, 11, 10, 0, 5, 7, 0, 9, 0],
           [4, 6, 0, 0, 12, 8, 1, 0, 3, 0, 0, 0], [2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
           [11, 9, 0, 0, 10, 6, 0, 8, 1, 0, 3, 5], [0, 4, 0, 1, 0, 0, 11, 7, 10, 12, 2, 0],
           [5, 8, 7, 0, 0, 2, 0, 0, 9, 0, 0, 6], [0, 0, 5, 0, 0, 0, 3, 12, 0, 4, 0, 10],
           [0, 3, 0, 4, 9, 0, 0, 0, 6, 8, 1, 0], [1, 2, 12, 0, 6, 0, 7, 0, 0, 0, 11, 0]]


# recursive function
def solver(puzzle, order, digits):
    d = len(puzzle)

    # each row with non zero elements
    row = [[x for x in puzzle[y] if x != 0] for y in range(0, d)]
    # each column with non zero elements
    column = [[puzzle[x][y]
               for x in range(0, d) if puzzle[x][y] != 0] for y in range(0, d)]

    # Boxes have been labeled (i,j) i.e. into n//order[0] * n//order[1] boxes
    box = {(i, j): [] for i in range(0, d // order[0])
           for j in range(0, d // order[1])}

    # adding elements to boxes
    [box[(i // order[0], j // order[1])].append(puzzle[i][j])
     for i in range(0, d) for j in range(0, d) if puzzle[i][j] != 0]

    # counting no of total zeros
    zeros = len([puzzle[x][y] for x in range(0, d)
                 for y in range(0, d) if puzzle[x][y] == 0])

    for x in range(0, d):
        for y in range(0, d):
            if puzzle[x][y] != 0:
                continue  # Proceed with next element if this is already filled
            else:
                # elements that are possible in this unfilled cell
                possibilities = digits.difference(set(row[x])).difference(
                    set(column[y])).difference(box[(x // order[0], y // order[1])])
                if possibilities:
                    # n keeps track of which number of possibility we are current iterating through
                    n = 0
                    for possibility in possibilities:
                        # reduce no of unfilled box because it is going to be filled with a possibility
                        zeros -= 1
                        # new copy list
                        new_puzzle = copy.deepcopy(puzzle)
                        # modification of list with possibility
                        new_puzzle[x][y] = possibility
                        # if this was last element to fill ,terminate to give answer
                        if zeros == 0:
                            return new_puzzle
                        # else iterate
                        result = solver(new_puzzle, order, digits)
                        # passes result to the previous recursion function as result has been obtained
                        if result:
                            return result
                        else:
                            # else increase no of zeros as it was a fail
                            n += 1
                            zeros += 1
                            # n+=1 is the nth possibility we are in
                            # if this was last possibility it was fail so return 0 for backtracking
                            if len(possibilities) == n:
                                return 0
                            else:  # else if still possibilities are left try them
                                continue
                else:
                    return 0  # if no possibilities return 0


def main(puzzle, order):
    # possible digits
    digits = {x for x in range(1, order[0] * order[1] + 1)}
    answer = solver(puzzle, order, digits)
    if answer:
        for x in range(len(answer)):
            for y in range(len(answer[x])):
                if (y + 1) % order[1] == 0 and y != 0:
                    print(f"{answer[x][y]:3d}", end=" |")
                else:
                    print(f"{answer[x][y]:3d}", end="")
            print()
            if (x + 1) % order[0] == 0 and x != 0:
                print("-" * ((3 * order[0] * order[1]) + order[0] * 2))
    else:
        print("Sorry, the puzzle has no solution")


main(puzzle1, order1)
main(puzzle2, order2)

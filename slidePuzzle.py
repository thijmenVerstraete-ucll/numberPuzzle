import random


def generatePuzzle(width, height):
    output = []

    # Exaple: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    num = 1
    row = []
    for i in range(1, height+1):
        for j in range(1, width+1):
            row.append(num)
            num += 1
        output.append(row)
        row = []
    output[-1][-1] = 0
    return output


def randomizePuzzle(puzzle):
    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle[i])):
            randRow = random.randint(0, len(puzzle)-1)
            randCol = random.randint(0, len(puzzle[0])-1)
            puzzle[i][j], puzzle[randRow][randCol] = puzzle[randRow][randCol], puzzle[i][j]
    return puzzle


def printPuzzle(puzzle):
    for i in puzzle:
        print(i)


def findPos(puzzle, num):
    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle)):
            if puzzle[i][j] == num:
                return [i, j]


def shift(puzzle, num, openPos):
    pos = findPos(puzzle, num)

    range = []
    range.append(pos[0])
    range.append(pos[1])

    range[0] -= openPos[0]
    range[1] -= openPos[1]

    if range == [-1, 0] or range == [0, -1] or range == [1, 0] or range == [0, 1]:
        puzzle[openPos[0]][openPos[1]], puzzle[pos[0]][pos[1]
                                                       ] = puzzle[pos[0]][pos[1]], puzzle[openPos[0]][openPos[1]]
    return puzzle


def start():
    width = 3
    height = 3

    sortedPuzzle = generatePuzzle(width, height)
    puzzle = randomizePuzzle(generatePuzzle(width, height))
    printPuzzle(puzzle)

    while sortedPuzzle != puzzle:
        openPos = findPos(puzzle, 0)
        inpt = int(input())
        puzzle = shift(puzzle, inpt, openPos)
        printPuzzle(puzzle)


start()

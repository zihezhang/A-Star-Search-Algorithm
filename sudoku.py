puzzle = [
    [2,0,9,0,0,0,6,0,0],
    [0,4,0,8,7,0,0,1,2],
    [8,0,0,0,1,9,0,4,0],
    [0,3,0,7,0,0,8,0,1],
    [0,6,5,0,0,8,0,3,0],
    [1,0,0,0,3,0,0,0,7],
    [0,0,0,6,5,0,7,0,9],
    [6,0,4,0,0,0,0,2,0],
    [0,8,0,3,0,1,4,5,0]
]


def solve(board):
    find = find_empty(board)
    if not find: #if there are no empties
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check(board, i, (row, col)):
            board[row][col] = i

            if solve(board): #recusively tries to finish the solution
                return True

            board[row][col] = 0

    return False


def check(board, number, position):
    # Check box
    x = position[1] // 3
    y = position[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)): #loops through row
        for j in range(len(board[0])): #loops through column
            if board[i][j] == 0:
                return (i, j)  

    return None

# a function to read the 
def read_img():
    # I wanted the user to have the liberty to choose the image
    print("Enter image name: ")
    image_url = input()
    #image url also conatins the image extension eg. .jpg or .png
    #reading in greayscale
    img = cv2.imread(image_url, img = cv2.imread(image_url, cv2.IMREAD_GRAYSCALE))


print_board(puzzle)
solve(puzzle)
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print_board(puzzle)

# Done with the help of https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
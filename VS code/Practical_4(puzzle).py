# Define the size of the grid
N = 9

def is_valid(board, row, col, num):
    # Check if num is not in the current row
    for x in range(N):
        if board[row][x] == num:
            return False
    
    # Check if num is not in the current column
    for x in range(N):
        if board[x][col] == num:
            return False

    # Check if num is not in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_location(board)
    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    for num in range(1, N + 1):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack
    
    return False

def find_empty_location(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

# Sample Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print("Sudoku puzzle solved:")
    print_board(board)
else:
    print("No solution exists")

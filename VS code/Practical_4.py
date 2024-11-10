import sys

# Function to check if the queen placement is valid
def is_safe(board, row, col, N):
    # Check this column on the upper side
    for i in range(row):
        if board[i] == col:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check the upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True

# Recursive utility function to solve N Queens using Branch and Bound
def solve_nqueens_util(board, row, N, solutions):
    if row >= N:
        # All queens are placed correctly, add the solution
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place this queen in board[row]
            board[row] = col
            # Recur to place the rest of the queens
            solve_nqueens_util(board, row + 1, N, solutions)

            # Backtrack, remove the queen from board[row] (Not required in Python due to list copy)

# Main function to solve the N-Queens problem using Branch and Bound
def solve_nqueens(N):
    # Initialize the board with -1 (meaning no queen is placed in any row)
    board = [-1] * N
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions

# Function to print the solution in a readable format
def print_solutions(solutions, N):
    for sol in solutions:
        print("Solution:")
        for i in range(N):
            row = ['.'] * N
            row[sol[i]] = 'Q'
            print(' '.join(row))
        print()

# Driver code
if __name__ == "__main__":
    N = int(input("Enter the number of queens: "))  # For example, 4 for a 4x4 board
    solutions = solve_nqueens(N)

    print(f"Total solutions for {N}-Queens problem: {len(solutions)}")
    print_solutions(solutions, N)

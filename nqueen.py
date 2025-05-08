# Check if it's safe to place a queen at (row, col)
def is_safe(board, row, col):
    # Iterate through all previously placed queens
    for r in range(row):
        c = board[r]
        # Check if there's a queen in the same column or diagonal
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True  # Safe to place the queen

# Recursive function to solve N-Queens using backtracking
def solve(board, row, solutions, n):
    # Base case: All queens are placed
    if row == n:
        solutions.append(board[:])  # Add a copy of the board to solutions
        return

    # Try placing queen in every column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen at (row, col)
            solve(board, row + 1, solutions, n)  # Recurse to next row
            board[row] = -1  # Backtrack: Remove queen

# Initializes the board and starts the solving process
def solve_n_queens(n):
    solutions = []  # To store all valid board configurations
    board = [-1] * n  # Represents queen positions: index = row, value = column
    solve(board, 0, solutions, n)
    return solutions

# Prints each solution in a readable board format
def print_solutions(solutions):
    for idx, board in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in board:
            print("".join("Q" if i == row else "." for i in range(len(board))))
        print()

# Run the solver for 8-Queens and display the result
n = 8
solutions = solve_n_queens(n)
print(f"Total Solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions)

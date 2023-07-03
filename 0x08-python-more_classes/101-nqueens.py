#!/usr/bin/python3

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""

    # Check the column on the upper side
    for i in range(row):
        if board[i] == col:
            return False

        # Check diagonals
        if board[i] - i == col - row or board[i] + i == col + row:
            return False

    return True


def solve_nqueens(n):
    """Solve the N-Queens problem"""

    def backtrack(board, row, solutions):
        """Backtracking function to find solutions"""

        if row == n:
            solutions.append(board[:])  # Make a copy of the board
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(board, row + 1, solutions)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * n
    solutions = []

    backtrack(board, 0, solutions)

    return solutions


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])

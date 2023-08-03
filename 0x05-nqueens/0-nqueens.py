import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check if there is a queen in the same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def print_board(board):
    n = len(board)
    for row in range(n):
        print([row, board[row]])

def solve_nqueens(n, row=0, board=None):
    if board is None:
        board = [-1] * n

    if row == n:
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board)
            board[row] = -1

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

if __name__ == "__main__":
    main()


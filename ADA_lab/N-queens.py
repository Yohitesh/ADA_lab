def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(row):
        if row == n:
            result.append([r[:] for r in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    result = []
    solve(0)
    return result

def print_solution(board):
    for row in board:
        line = ""
        for col in row:
            line += "Q " if col == 1 else ". "
        print(line.strip())
    print()

# Example usage:
n = 4
solutions = solve_n_queens(n)

print(f"Total solutions for {n}-Queens: {len(solutions)}\n")
for sol in solutions:
    print_solution(sol)

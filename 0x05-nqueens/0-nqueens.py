#!/usr/bin/python3
import sys


def print_usage_and_exit(message, status=1):
    print(message)
    sys.exit(status)


def is_safe(queens, row, col):
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n):
    solutions = []


    def backtrack(row, queens):
        if row == n:
            solution = [[r, queens[r]] for r in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                backtrack(row + 1, queens)
                queens.pop()

    backtrack(0, [])
    return solutions


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

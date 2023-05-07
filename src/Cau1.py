class EightQueenSolver:
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.results = []

    def is_conflict(self, r1, c1, r2, c2):
        if r1 == r2 or c1 == c2 or abs(r1-r2) == abs(c1-c2):
            return True
        else:
            return False

    def is_valid(self, row, col):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1 and (i != row or j != col) and self.is_conflict(i, j, row, col):
                    return False
        return True

    def backtracking(self, row):
        if row == 8:
            self.results.append([row[:] for row in self.board])
            return

        for col in range(8):
            if self.is_valid(row, col):
                self.board[row][col] = 1
                self.backtracking(row+1)
                self.board[row][col] = 0

    def solve(self):
        self.results = []
        self.backtracking(0)

        if len(self.results) == 0:
            print("UNSOLVABLE")
        else:
            self.print_results()

    def print_board(self, board):
        for row in board:
            print(' '.join(['Q' if x == 1 else '.' for x in row]))

    def print_results(self):
        for i, result in enumerate(self.results):
            print(f"result {i+1}:")
            self.print_board(result)
            print()


class NQueenSolver:
    def __init__(self, N: int):
        self.N = N
        self.board = [[0 for i in range(N)] for j in range(N)]
        self.results = []

    def is_conflict(self, r1, c1, r2, c2):
        if r1 == r2 or c1 == c2 or abs(r1-r2) == abs(c1-c2):
            return True
        else:
            return False

    def is_valid(self, row, col):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 1 and (i != row or j != col) and self.is_conflict(i, j, row, col):
                    return False
        return True

    def backtracking(self, row):
        if row == self.N:
            self.results.append([row[:] for row in self.board])
            return

        for col in range(self.N):
            if self.is_valid(row, col):
                self.board[row][col] = 1
                self.backtracking(row+1)
                self.board[row][col] = 0

    def solve(self):
        self.results = []
        self.backtracking(0)

        if len(self.results) == 0 or self.N <= 0:
            print("UNSOLVABLE")
        else:
            self.print_results()

    def print_board(self, board):
        for row in board:
            print(' '.join(['Q' if x == 1 else '.' for x in row]))

    def print_results(self):
        if self.N <= 0:
            return
        for i, result in enumerate(self.results):
            print(f"result {i+1}:")
            self.print_board(result)
            print()


# solver1 = EightQueenSolver()
# solver1.solve()

solver2 = NQueenSolver(100 )
solver2.solve()

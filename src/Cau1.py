class EightQueenSolver:
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]

    def print_board(self):
        for row in self.board:
            print(' '.join(['Q' if x == 1 else '.' for x in row]))

    def is_conflict(self, row1, col1, row2, col2):
        if row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2):
            return True
        else:
            return False

    def is_valid(self, row, col):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1 and (i != row or j != col) and self.is_conflict(i, j, row, col):
                    return False
        return True

    def backtrack(self, row):
        if row == 8:
            return True

        for col in range(8):
            if self.is_valid(row, col):
                self.board[row][col] = 1
                if self.backtrack(row+1):
                    return True
                self.board[row][col] = 0

        return False

    def solve(self):
        self.backtrack(0)
        self.print_board()
        



class NQueenSolver:
    def __init__(self,N):
        self.n=N
        self.board = [[0 for i in range(N)] for j in range(N)]

    def print_board(self):
        for row in self.board:
            print(' '.join(['Q' if x == 1 else '.' for x in row]))

    def is_conflict(self, row1, col1, row2, col2):
        if row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2):
            return True
        else:
            return False

    def is_valid(self, row, col):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1 and (i != row or j != col) and self.is_conflict(i, j, row, col):
                    return False
        return True

    def backtracking(self, row):
        if row == self.n:
            return True

        for col in range(self.n):
            if self.is_valid(row, col):
                self.board[row][col] = 1
                if self.backtracking(row+1):
                    return True
                self.board[row][col] = 0

        return False

    def solve(self):
        if self.backtracking(0)==False:
            print("UNSOLVABLE")
        else:
            self.backtracking(0)
            self.print_board()


solver = EightQueenSolver()
solver.solve()           
solver1 = NQueenSolver(6)
solver1.solve()
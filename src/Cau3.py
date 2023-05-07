from pysat.solvers import Glucose3
from pysat.formula import CNF

class EightQueenSolver:
    def __init__(self):
        self.n = 8
        self.solver = Glucose3()
        self.variables = {}
        self.clauses = CNF()
        self.variables_inv  = {}

    def get_var_id(self, row, col):
        return self.variables[(row, col)]

    def add_variables(self):
        for i in range(self.n):
            for j in range(self.n):
                var_id = len(self.variables) + 1
                self.variables[(i, j)] = var_id
                self.variables_inv[var_id] = (i, j)

    def add_clauses(self):
        # Each row should contain only one queen
        for i in range(self.n):
            clause = [self.get_var_id(i, j) for j in range(self.n)]
            self.clauses.append(clause)
            for j1 in range(self.n):
                for j2 in range(j1 + 1, self.n):
                    clause = [-self.get_var_id(i, j1), -self.get_var_id(i, j2)]
                    self.clauses.append(clause)

        # Each column should contain only one queen
        for j in range(self.n):
            clause = [self.get_var_id(i, j) for i in range(self.n)]
            self.clauses.append(clause)
            for i1 in range(self.n):
                for i2 in range(i1 + 1, self.n):
                    clause = [-self.get_var_id(i1, j), -self.get_var_id(i2, j)]
                    self.clauses.append(clause)

        # Each diagonal should contain only one queen
        for i in range(self.n):
            for j in range(self.n):
                for k in range(1, self.n):
                    if i - k >= 0 and j - k >= 0:
                        clause = [-self.get_var_id(i, j), -self.get_var_id(i - k, j - k)]
                        self.clauses.append(clause)
                    if i + k < self.n and j - k >= 0:
                        clause = [-self.get_var_id(i, j), -self.get_var_id(i + k, j - k)]
                        self.clauses.append(clause)
                    if i - k >= 0 and j + k < self.n:
                        clause = [-self.get_var_id(i, j), -self.get_var_id(i - k, j + k)]
                        self.clauses.append(clause)
                    if i + k < self.n and j + k < self.n:
                        clause = [-self.get_var_id(i, j), -self.get_var_id(i + k, j + k)]
                        self.clauses.append(clause)

    def solve(self):
        self.add_variables()
        self.add_clauses()
        for clause in self.clauses:
            self.solver.add_clause(clause)
        if self.solver.solve():
            solution = [['.' for j in range(self.n)] for i in range(self.n)]
            model = self.solver.get_model()
            for i in range(len(model)):
                if model[i] > 0:
                    row, col = self.variables_inv[model[i]]
                    solution[row][col] = 'Q'
            for row in solution:
                print(' '.join(row))
        else:
            print("UNSOLVABLE")


class NQueenSolver(EightQueenSolver): #inherit class EightQueenSolver
    def __init__(self, n):
        self.n = n
        self.solver = Glucose3()
        self.variables = {}
        self.clauses = CNF()
        self.variables_inv  = {}

print("Solution for EightQueenSolver:")
solver = EightQueenSolver()
solution = solver.solve()

print("Solution for NQueenSolver with n = 10:")
solver = NQueenSolver(10)
solution = solver.solve()

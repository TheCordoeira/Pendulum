#For solving A v = lambda v - Equation Systems using eingenvalues and eigenvectors

import sympy as sp

# Symbolic Variables
m, l, a, G, g, phi, p = sp.symbols('m l a G g phi p')

# Matrix A
A = sp.Matrix([
    [0, (2 / (m * l**2)) - 1],
    [-m * a * l * G**2 * sp.sin(phi) - m * g * l * sp.cos(phi), 0]
])

# Eingenvalues and Eigenvectors
eigenvals = A.eigenvals()
eigenvects = A.eigenvects()

# Terminal Print
print("Autovalores:")
for eigenval in eigenvals:
    print(eigenval)

print("\nAutovetores:")
for eigenvect in eigenvects:
    print("Autovalor:", eigenvect[0])
    print("Multiplicidade:", eigenvect[1])
    print("Autovetores:")
    for vect in eigenvect[2]:
        print(vect)

# Symbolic Solver
X, P = sp.symbols('X P')
v = sp.Matrix([X, P])
solutions = sp.solve(A * v - eigenvals[list(eigenvals.keys())[0]] * v, [X, P])

print("\nSolução do sistema (A * v = lambda * v):")
print(solutions)

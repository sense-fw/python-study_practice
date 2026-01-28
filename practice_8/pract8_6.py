def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def max_in_rows(matrix):
    return [max(row) for row in matrix]

def min_in_columns(matrix):
    n = len(matrix)
    return [min(matrix[i][j] for i in range(n)) for j in range(n)]

n = int(input('Введите порядок квадратной матрицы n: '))
A = input_matrix(n)

max_rows = max_in_rows(A)
min_cols = min_in_columns(A)

print('Максимальные элементы в каждой строке:', max_rows)
print('Минимальные элементы в каждом столбце:', min_cols)
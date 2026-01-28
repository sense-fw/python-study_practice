def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

n = int(input('Введите порядок матрицы n: '))
A = input_matrix(n)

if is_symmetric(A):
    print('Матрица симметрична относительно главной диагонали')
else:
    print('Матрица несимметрична относительно главной диагонали')
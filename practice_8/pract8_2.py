def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    
    # Проверяем строки
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    # Проверяем столбцы
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    
    return True

n = int(input('Введите порядок матрицы n: '))
A = input_matrix(n)

if is_magic_square(A):
    print('Матрица является магическим квадратом')
else:
    print('Матрица не является магическим квадратом')
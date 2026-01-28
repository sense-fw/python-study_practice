def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def swap_max_diag_row(matrix, m):
    n = len(matrix)
    # ищем строку с максимальным элементом на главной диагонали
    max_value = matrix[0][0]
    max_row_index = 0
    for i in range(n):
        if matrix[i][i] > max_value:
            max_value = matrix[i][i]
            max_row_index = i
    # меняем строки местами
    matrix[max_row_index], matrix[m-1] = matrix[m-1], matrix[max_row_index]
    return matrix

n = int(input('Введите порядок матрицы n: '))
A = input_matrix(n)
m = int(input('Введите номер строки m для обмена: '))

A = swap_max_diag_row(A, m)

print('Матрица после перестановки строк:')
for row in A:
    print(row)
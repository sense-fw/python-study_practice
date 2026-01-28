def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def rows_equal_columns(matrix):
    n = len(matrix)
    matching_indices = []
    for k in range(n):
        row = matrix[k]
        col = [matrix[i][k] for i in range(n)]
        if row == col:
            matching_indices.append(k + 1)  # +1 для привычной нумерации с 1
    return matching_indices

n = int(input('Введите порядок матрицы n: '))
A = input_matrix(n)

matching_k = rows_equal_columns(A)

if matching_k:
    print('Номера строк k, совпадающих с k-м столбцом:', matching_k)
else:
    print('Таких строк нет')
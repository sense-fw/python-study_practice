def input_matrix(M, N):
    A = []
    for i in range(M):
        row = []
        for j in range(N):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def multiply_rows_with_value(matrix, c, d):
    rows_indices = []
    for i, row in enumerate(matrix):
        if c in row:
            rows_indices.append(i + 1)  # номера строк с 1
            matrix[i] = [elem * d for elem in row]
    return rows_indices, matrix

M = int(input('Введите количество строк M: '))
N = int(input('Введите количество столбцов N: '))
R = input_matrix(M, N)
c = float(input('Введите значение c: '))
d = float(input('Введите множитель d: '))

rows_indices, R = multiply_rows_with_value(R, c, d)

if rows_indices:
    print('Номера строк, содержащих хотя бы один элемент c:', rows_indices)
else:
    print('Строк с элементом c нет')

print('Матрица после умножения строк на d:')
for row in R:
    print(row)
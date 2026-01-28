def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def sum_of_row_with_min_elem(matrix):
    n = len(matrix)
    min_value = matrix[0][0]
    min_row_index = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row_index = i
    row_sum = sum(matrix[min_row_index])
    return row_sum

n = int(input('Введите порядок матрицы n: '))
A = input_matrix(n)

row_sum = sum_of_row_with_min_elem(A)
print('Сумма элементов строки с минимальным элементом:', row_sum)
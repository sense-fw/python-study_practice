def input_matrix(rows, cols):
    A = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def min_max_sum_rows(matrix):
    min_sum = float('inf')
    max_sum = float('-inf')
    min_row = max_row = []

    for row in matrix:
        s = sum(row)
        if s > max_sum:
            max_sum = s
            max_row = row
        if s < min_sum:
            min_sum = s
            min_row = row

    return min_row, min_sum, max_row, max_sum

rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))
A = input_matrix(rows, cols)

min_row, min_sum, max_row, max_sum = min_max_sum_rows(A)

print('Строка с минимальной суммой элементов:', min_row, 'Сумма:', min_sum)
print('Строка с максимальной суммой элементов:', max_row, 'Сумма:', max_sum)
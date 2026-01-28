def input_matrix(n, m):
    A = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def is_sorted(row):
    return all(row[i] <= row[i+1] for i in range(len(row)-1)) or \
           all(row[i] >= row[i+1] for i in range(len(row)-1))

def max_in_sorted_rows(matrix):
    max_elem = None
    for row in matrix:
        if is_sorted(row):
            row_max = max(row)
            if max_elem is None or row_max > max_elem:
                max_elem = row_max
    return max_elem

rows = int(input('Введите количество строк: '))
cols = int(input('Введите количество столбцов: '))
A = input_matrix(rows, cols)

result = max_in_sorted_rows(A)

if result is not None:
    print('Максимальный элемент среди отсортированных строк:', result)
else:
    print('Нет отсортированных строк')
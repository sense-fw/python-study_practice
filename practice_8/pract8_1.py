def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def sum_and_count_above_diagonal(matrix):
    total = 0
    count = 0
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                total += matrix[i][j]
                count += 1
    return total, count

n = int(input('Введите размер матрицы N: '))
A = input_matrix(n)
total, count = sum_and_count_above_diagonal(A)

print('Сумма положительных элементов над главной диагональю:', total)
print('Количество положительных элементов над главной диагональю:', count)
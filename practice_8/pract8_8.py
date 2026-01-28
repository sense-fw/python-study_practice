def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def count_and_max_divisible(matrix, k):
    count = 0
    max_elem = None
    for row in matrix:
        for elem in row:
            if elem % k == 0:
                count += 1
                if max_elem is None or elem > max_elem:
                    max_elem = elem
    return count, max_elem

n = int(input('Введите порядок матрицы n: '))
A = input_matrix(n)
k = int(input('Введите число k: '))

count, max_elem = count_and_max_divisible(A, k)

print('Количество элементов, кратных k:', count)
if max_elem is not None:
    print('Наибольший элемент, кратный k:', max_elem)
else:
    print('Элементов, кратных k, нет')
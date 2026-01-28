def input_matrix(n, m):
    A = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def sort_rows(matrix):
    for row in matrix:
        row.sort()
    return matrix

n = int(input('Введите количество строк n: '))
m = int(input('Введите количество столбцов m: '))
A = input_matrix(n, m)

A_sorted = sort_rows(A)

print('Матрица после упорядочивания строк по возрастанию:')
for row in A_sorted:
    print(row)
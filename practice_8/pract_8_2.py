def input_matrix(n):
    A = []
    for i in range(n):
        m = []
        for j in range(n):
            print('Введите [', i, ',', j, '] элемент: ')
            m.append(float(input()))
        A.append(m)
    return A

def print_matrix(A):
    print()
    for row in A:
        for x in row:
            print(f"{x:8.2f}", end=" ")
        print()

def transpose_matrix(A):
    n = len(A)
    T = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            T[j][i] = A[i][j]
    return T


n = int(input('Введите размерность матрицы n: '))
A = input_matrix(n)
print('\nИсходная матрица:')
print_matrix(A)
T = transpose_matrix(A)
print('\nТранспонированная матрица:')
print_matrix(T)
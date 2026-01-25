def read_matrix_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        n = int(f.readline())
        A = []
        for _ in range(n):
            A.append(list(map(float, f.readline().split())))
        k = int(f.readline()) - 1
    return A, k


def write_matrix_to_file(f, title, A):
    f.write(title + '\n')
    for row in A:
        for x in row:
            f.write(f"{x:8.2f} ")
        f.write('\n')
    f.write('\n')


def divide_row(A, k):
    n = len(A)
    if not (0 <= k < n):
        return None

    diag = A[k][k]
    if diag == 0:
        return None

    for j in range(n):
        A[k][j] /= diag

    return A


def transpose_matrix(A):
    n = len(A)
    T = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            T[j][i] = A[i][j]
    return T

input_file = r'C:\Users\777\Desktop\Учеба\1 КУРС\папка с кодом\files_code\Sharova_ZIT-251_vvod.txt'
output_file = r'C:\Users\777\Desktop\Учеба\1 КУРС\папка с кодом\files_code\Sharova_ZIT-251_vivod.txt'

A, k = read_matrix_from_file(input_file)

with open(output_file, 'w', encoding='utf-8') as f:
    write_matrix_to_file(f, 'Исходная матрица:', A)

    B = divide_row([row[:] for row in A], k)
    if B is None:
        f.write('Деление выполнить невозможно\n\n')
    else:
        write_matrix_to_file(
            f,
            f'Матрица после деления {k + 1}-й строки на диагональный элемент:',
            B
        )

    T = transpose_matrix(A)
    write_matrix_to_file(f, 'Транспонированная матрица:', T)

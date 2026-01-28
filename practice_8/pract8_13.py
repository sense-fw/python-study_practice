def input_matrix(M, N):
    A = []
    for i in range(M):
        row = []
        for j in range(N):
            row.append(float(input(f'Введите элемент [{i+1},{j+1}]: ')))
        A.append(row)
    return A

def min_in_even_rows(matrix):
    min_values = []
    for i in range(1, len(matrix), 2):  # чётные строки: 2-я, 4-я… (индексы 1,3,…)
        min_values.append(min(matrix[i]))
    return min_values

M = int(input('Введите количество строк M: '))
N = int(input('Введите количество столбцов N: '))
A = input_matrix(M, N)

min_values = min_in_even_rows(A)

for idx, val in enumerate(min_values, start=2):
    print(f'Наименьший элемент {idx}-й строки:', val)
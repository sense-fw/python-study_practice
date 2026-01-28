A = []
n = int(input('Введите количество элементов массива: '))

print('Введите элементы массива:')
for i in range(n):
    A.append(int(input(f'Элемент {i}: ')))

found = False

for i in range(n):
    for j in range(i + 1, n):
        if A[i] == A[j]:
            print(f'Повторяющийся элемент: {A[i]}, индексы: {i}, {j}')
            found = True

if not found:
    print('Повторяющихся элементов нет')
A = []
n = int(input('Введите количество элементов списка: '))

print('Введите элементы списка:')
for i in range(n):
    A.append(int(input(f'Элемент {i}: ')))

repeats = []

for i in range(n):
    for j in range(i + 1, n):
        if A[i] == A[j] and A[i] not in repeats:
            repeats.append(A[i])

if repeats:
    print('Повторяющиеся элементы:', repeats)
else:
    print('Повторяющихся элементов нет')
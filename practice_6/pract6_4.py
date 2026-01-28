n = int(input('Введите количество элементов массива: '))

A = []
for i in range(n):
    A.append(int(input(f'Введите элемент {i}: ')))

max_value = A[0]
max_index = 0

for i in range(1, n):
    if A[i] > max_value:
        max_value = A[i]
        max_index = i

print('Массив:', A)
print('Максимальный элемент:', max_value)
print('Порядковый номер максимального элемента:', max_index + 1)
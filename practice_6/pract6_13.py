A = []
n = int(input('Введите количество элементов массива: '))

print('Введите элементы массива:')
for i in range(n):
    A.append(int(input(f'Элемент {i}: ')))

max_index = 0
min_index = 0

for i in range(1, n):
    if A[i] > A[max_index]:
        max_index = i
    if A[i] < A[min_index]:
        min_index = i

A[max_index], A[min_index] = A[min_index], A[max_index]

print('Массив после замены максимального и минимального элементов:')
print(A)
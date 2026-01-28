A = []
n = int(input('Введите количество элементов массива: '))

print('Введите вещественные элементы массива:')
for i in range(n):
    A.append(float(input(f'Элемент {i}: ')))

min_abs = A[0]
for x in A:
    if abs(x) < abs(min_abs):
        min_abs = x

print('Минимальный по модулю элемент:', min_abs)

print('Массив в обратном порядке:')
for x in A[::-1]:
    print(x, end=' ')
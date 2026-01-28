n = int(input('Введите длину массива: '))

D = []
for i in range(n):
    D.append(int(input(f'Введите элемент {i}: ')))

sum_odd_index = 0
for i in range(n):
    if i % 2 != 0:
        sum_odd_index += D[i]

print('Массив D:', D)
print('Сумма элементов с нечетными индексами:', sum_odd_index)
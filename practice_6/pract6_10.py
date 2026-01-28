A = []
n = int(input('Введите количество элементов списка: '))

print('Введите элементы списка:')
for i in range(n):
    A.append(int(input(f'Элемент {i}: ')))

max_even = None

for x in A:
    if x % 2 == 0:
        if max_even is None or x > max_even:
            max_even = x

if max_even is not None:
    print('Наибольший элемент, делящийся на 2 без остатка:', max_even)
else:
    print('В списке нет элементов, делящихся на 2 без остатка')
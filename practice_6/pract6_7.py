A = []
n = int(input('Введите количество элементов массива: '))

print('Введите элементы массива:')
for i in range(n):
    A.append(int(input(f'Элемент {i}: ')))

sum_even = 0
prod_even = 1
found = False

for i in range(0, n, 2):
    sum_even += A[i]
    prod_even *= A[i]
    found = True

print('Массив:', A)
print('Сумма элементов с чётными номерами:', sum_even)

if found:
    print('Произведение элементов с чётными номерами:', prod_even)
else:
    print('Элементов с чётными номерами нет')
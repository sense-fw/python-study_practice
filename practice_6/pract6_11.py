A = []
n = int(input('Введите количество элементов списка: '))

print('Введите элементы списка:')
for i in range(n):
    A.append(int(input(f'Элемент {i}: ')))

min_odd = None

for x in A:
    if x % 2 != 0:  
        if min_odd is None or x < min_odd:
            min_odd = x

if min_odd is not None:
    print('Наименьший нечётный элемент списка:', min_odd)
else:
    print('В списке нет нечётных элементов')
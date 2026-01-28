A = []

print('Введите 10 целых чисел:')
for i in range(10):
    A.append(int(input(f'Элемент {i}: ')))

max_elem = A[0]
for x in A:
    if x > max_elem:
        max_elem = x

less = 0
greater = 0

for x in A:
    if x < max_elem:
        less += 1
    elif x > max_elem:
        greater += 1

print('Максимальный элемент:', max_elem)
print('Количество элементов меньше максимального:', less)
print('Количество элементов больше максимального:', greater)
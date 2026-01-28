A = []

print('Введите 10 целых чисел:')
for i in range(10):
    A.append(int(input(f'Элемент {i}: ')))

print('Пары соседних отрицательных чисел:')

found = False
for i in range(9):
    if A[i] < 0 and A[i + 1] < 0:
        print(A[i], A[i + 1])
        found = True

if not found:
    print('Таких пар нет')
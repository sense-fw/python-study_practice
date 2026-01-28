A = []
n = int(input('Введите количество элементов списка: '))

print('Введите элементы списка:')
for i in range(n):
    A.append(int(input(f'Элемент {i}: ')))

found = False

for i in range(n):
    for j in range(i + 1, n):
        if A[i] == A[j]:
            print('Повторяющийся элемент:', A[i])
            found = True
            break
    if found:
        break

if not found:
    print('Повторяющихся элементов нет')
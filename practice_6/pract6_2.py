N = int(input('Введите количество элементов массива: '))

arr = []
for i in range(N):
    arr.append(int(input(f'Введите элемент {i + 1}: ')))

min_element = arr[0]
min_index = 0

for i in range(1, N):
    if arr[i] < min_element:
        min_element = arr[i]
        min_index = i

print('Минимальный элемент массива:', min_element)
print('Индекс минимального элемента:', min_index)
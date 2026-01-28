n = int(input('Введите количество элементов массива: '))

arr = []
for i in range(n):
    arr.append(int(input(f'Введите элемент {i + 1}: ')))

max_element = arr[0]
for x in arr:
    if x > max_element:
        max_element = x

print('Максимальный элемент массива:', max_element)

print('Массив в обратном порядке:')
for x in arr[::-1]:
    print(x, end=' ')
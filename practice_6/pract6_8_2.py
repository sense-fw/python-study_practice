n = int(input("Введите количество элементов: "))
arr = []

print("Введите элементы:")

for i in range(n):
    arr.append(float(input()))

original = arr.copy()

average = sum(arr) / n

for i in range(n):
    if arr[i] == 0:
        arr[i] = average

print("Исходный массив:", original)
print("Среднее арифметическое:", average)
print("Массив после замены нулей:", arr)

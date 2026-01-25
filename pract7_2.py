def swap_first_last(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]  

m = int(input("Введите длину массива: "))
A = []

print("Введите элементы массива:")
for i in range(m):
    A.append(float(input()))  

original = A.copy()
swap_first_last(A)

print("Исходный массив:", original)
print("Массив после замены первого и последнего элементов:", A)

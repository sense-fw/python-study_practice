n = int(input("Введите количество элементов: "))
print("Введите элементы: ")
arr = []

for i in range(n):
    arr.append(float(input()))

summa = 0
proizv = 1

for x in arr:
    summa += x
    proizv *= x

print("Сумма:", summa)
print("Произведение:", proizv)
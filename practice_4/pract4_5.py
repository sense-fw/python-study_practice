n = int(input('Введите натуральное число n: '))
s = 0

for i in range(1, n + 1):
    s += i ** 3

print('Сумма кубов:', s)

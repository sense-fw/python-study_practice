n = int(input('Введите натуральное число n: '))

fact = 1
s = 0

for i in range(1, n + 1):
    fact *= i      
    s += fact     

print('Сумма факториалов:', s)

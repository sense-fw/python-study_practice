def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    n = len(digits)
    return sum(d ** n for d in digits) == num

k = int(input('Введите число k: '))

print('Числа Армстронга от 1 до', k, ':')
for i in range(1, k + 1):
    if is_armstrong(i):
        print(i, end=' ')
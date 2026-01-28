def count_numbers_with_digits(N, a, b, c):
    digits = {str(a), str(b), str(c)}
    count = 0
    for num in range(100, N + 1):
        if all(d in digits for d in str(num)):
            count += 1
    return count

N = int(input('Введите N (210 < N < 231): '))
a = int(input('Введите цифру a: '))
b = int(input('Введите цифру b: '))
c = int(input('Введите цифру c: '))

print('Количество чисел, составленных из цифр a, b, c:', count_numbers_with_digits(N, a, b, c))
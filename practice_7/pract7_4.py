def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def divide_fractions(a, b, c, d):
    num = a * d
    den = b * c
    common = gcd(num, den)
    return num // common, den // common

A = int(input('Введите числитель первой дроби A: '))
B = int(input('Введите знаменатель первой дроби B: '))
C = int(input('Введите числитель второй дроби C: '))
D = int(input('Введите знаменатель второй дроби D: '))

numerator, denominator = divide_fractions(A, B, C, D)

print(f'Результат деления дроби A/B на C/D в несократимой форме: {numerator}/{denominator}')
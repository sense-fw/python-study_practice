def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def subtract_fractions(a, b, c, d):
    numerator = a * d - b * c
    denominator = b * d
    common = gcd(abs(numerator), denominator)
    return numerator // common, denominator // common

A = int(input('Введите числитель первой дроби A: '))
B = int(input('Введите знаменатель первой дроби B: '))
C = int(input('Введите числитель второй дроби C: '))
D = int(input('Введите знаменатель второй дроби D: '))

numerator, denominator = subtract_fractions(A, B, C, D)

print(f'Результат вычитания дроби A/B - C/D в несократимой форме: {numerator}/{denominator}')
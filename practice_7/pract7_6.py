def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

A = int(input('Введите число A: '))
B = int(input('Введите число B: '))

nod = gcd(A, B)
nok = lcm(A, B)

print('Наибольший общий делитель (НОД):', nod)
print('Наименьшее общее кратное (НОК):', nok)
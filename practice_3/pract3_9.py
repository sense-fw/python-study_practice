import math

a = float(input('Введите значение стороны a: '))
b = float(input('Введите значение стороны b: '))
c = float(input('Введите значение стороны c: '))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь треугольника:", S)
else:
    print("Треугольник с такими сторонами не существует")

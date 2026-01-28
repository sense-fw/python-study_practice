import math

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def input_triangle(number):
    print(f'Треугольник {number}:')
    a = float(input('Введите первый катет: '))
    b = float(input('Введите второй катет: '))
    return hypotenuse(a, b)

h1 = input_triangle(1)
h2 = input_triangle(2)

print('Гипотенуза первого треугольника:', h1)
print('Гипотенуза второго треугольника:', h2)

if h1 > h2:
    print('Гипотенуза первого треугольника больше')
elif h2 > h1:
    print('Гипотенуза второго треугольника больше')
else:
    print('Гипотенузы равны')
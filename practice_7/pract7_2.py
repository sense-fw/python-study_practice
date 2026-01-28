import math

def area_triangle(base, height):
    return 0.5 * base * height

def area_hexagon(a):
    height = a * math.sqrt(3) / 2
    return 6 * area_triangle(a, height)

a = float(input('Введите сторону правильного шестиугольника: '))
print('Площадь правильного шестиугольника:', area_hexagon(a))
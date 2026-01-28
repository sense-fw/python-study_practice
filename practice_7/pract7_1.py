import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

print('Выберите фигуру для вычисления площади:')
print('1 - Круг')
print('2 - Прямоугольник')
print('3 - Треугольник')

choice = int(input('Ваш выбор: '))

if choice == 1:
    r = float(input('Введите радиус круга: '))
    print('Площадь круга:', area_circle(r))
elif choice == 2:
    l = float(input('Введите длину прямоугольника: '))
    w = float(input('Введите ширину прямоугольника: '))
    print('Площадь прямоугольника:', area_rectangle(l, w))
elif choice == 3:
    b = float(input('Введите основание треугольника: '))
    h = float(input('Введите высоту треугольника: '))
    print('Площадь треугольника:', area_triangle(b, h))
else:
    print('Некорректный выбор')
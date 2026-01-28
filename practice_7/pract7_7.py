def area_right_triangle(a, b):
    return 0.5 * a * b

def area_rectangle(a, b):
    return a * b

X = float(input('Введите сторону X: '))
Y = float(input('Введите сторону Y: '))
Z = float(input('Введите сторону Z: '))
T = float(input('Введите сторону T: '))

triangle_area = area_right_triangle(X, Y)
rectangle_area = area_rectangle(Z, T)

total_area = triangle_area + rectangle_area

print('Площадь четырехугольника:', total_area)
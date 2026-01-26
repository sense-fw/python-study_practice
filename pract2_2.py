import math

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))

abs_xy = abs(x - y)

numerator = x + 3 * abs_xy + x**2
denominator = abs_xy * z + x**2

s = 5 * math.atan(x) - (1/4) * math.acos(x) * (numerator / denominator)

print(f"s = {s:.3f}")
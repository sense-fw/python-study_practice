import math

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))

numerator = math.exp(abs(x - y)) * (abs(x - y) ** (x + y))
denominator = math.atan(x) + math.atan(z)
term1 = numerator / denominator
term2 = (x**6 + (math.log(y))**2) ** (1/3)  

s = term1 + term2
print(f"Сумма s = {s:.4f}")
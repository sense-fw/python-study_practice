def power_div_fact(x, n):
    if n == 0:
        return 1  # x^0 / 0! = 1
    return (x ** n) / factorial(n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

x = float(input("Введите X: "))
n = int(input("Введите N: "))

result = power_div_fact(x, n)
print(f"x^{n} / {n}! = {result}")
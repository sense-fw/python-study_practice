def remainder(a, b):
    if a < b:
        return a
    return remainder(a - b, b)

a = int(input("Введите a: "))
b = int(input("Введите b: "))

res = remainder(a, b)
print(f"Остаток от деления {a} на {b} = {res}")
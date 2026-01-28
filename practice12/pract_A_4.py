def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

N = int(input("Введите число N: "))
result = sum_digits(N)
print(f"Сумма цифр числа {N} = {result}")
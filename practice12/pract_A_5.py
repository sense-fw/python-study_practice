def print_digits_reverse(n):
    print(n % 10, end=' ')  
    if n // 10 != 0:
        print_digits_reverse(n // 10)

N = int(input("Введите число N: "))
print("Цифры числа в обратном порядке:")
print_digits_reverse(N)
print()
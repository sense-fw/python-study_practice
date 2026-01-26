n = int(input("Введите число: "))

if n <= 1:
    print("Число не является простым")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Число простое")
    else:
        print("Число не является простым")

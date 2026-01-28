def is_prime(n, d=2):
    if n <= 2:
        return n == 2
    if d * d > n:  # дошли до корня из n
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)

n = int(input("Введите число n (>1): "))

if is_prime(n):
    print("YES")
else:
    print("NO")
def is_prime(n, d=2):
    if n <= 2:
        return n == 2
    if n % d == 0:
        return False
    if d * d > n:
        return True
    return is_prime(n, d + 1)

n = int(input("Введите число n (>1): "))

if is_prime(n):
    print("YES")
else:
    print("NO")
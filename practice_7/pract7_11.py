def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes(n):
    twins = []
    for i in range(n, 2 * n - 1):
        if is_prime(i) and is_prime(i + 2):
            twins.append((i, i + 2))
    return twins

n = int(input('Введите число n (>2): '))
for pair in twin_primes(n):
    print('Пара близнецов:', pair)
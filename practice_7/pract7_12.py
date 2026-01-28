def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total

def friendly_numbers(N):
    pairs = []
    for a in range(2, N):
        b = sum_of_divisors(a)
        if b > a and b <= N and sum_of_divisors(b) == a:
            pairs.append((a, b))
    return pairs

N = int(input('Введите число N: '))

for pair in friendly_numbers(N):
    print('Дружеская пара:', pair)
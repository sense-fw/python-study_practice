def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_binary_palindrome(num):
    bin_str = bin(num)[2:]  # преобразуем число в двоичную строку без '0b'
    return bin_str == bin_str[::-1]

n = int(input('Введите число n: '))

print('Простые числа с палиндромной двоичной записью до', n, ':')
for i in range(2, n + 1):
    if is_prime(i) and is_binary_palindrome(i):
        print(i, end=' ')
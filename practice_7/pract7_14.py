def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

M = int(input('Введите M: '))
N = int(input('Введите N: '))

max_div_count = 0
numbers = []

for num in range(M, N + 1):
    div_count = count_divisors(num)
    if div_count > max_div_count:
        max_div_count = div_count
        numbers = [num]
    elif div_count == max_div_count:
        numbers.append(num)

print('Числа с наибольшим количеством делителей:', numbers)
print('Количество делителей:', max_div_count)
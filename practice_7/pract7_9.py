def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def steps_to_zero(num):
    count = 0
    while num != 0:
        num -= sum_of_digits(num)
        count += 1
    return count

n = int(input('Введите число: '))
print('Количество действий до нуля:', steps_to_zero(n))
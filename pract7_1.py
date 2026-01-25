# функция проверяет, делится ли число на каждую свою цифру
def is_dividing(num):
    temp = num
    while temp > 0:
        digit = temp % 10
        if digit == 0 or num % digit != 0:
            return False
        temp //= 10
    return True

# процедура выводит числа
def print_numbers(n):
    print("Числа, делящиеся на каждую свою цифру до", n, ":")
    for i in range(1, n + 1):
        if is_dividing(i):
            print(i, end=" ")
    print() 

n = int(input("Введите n: "))
print_numbers(n)

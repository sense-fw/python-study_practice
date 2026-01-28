def find_max():
    n = int(input())
    if n == 0:
        return 0  # завершение последовательности
    else:
        m = find_max()  # рекурсивно считываем дальше
        return n if n > m else m

print("Введите последовательность чисел (0 для завершения):")
maximum = find_max()
print(f"Максимальное число в последовательности: {maximum}")
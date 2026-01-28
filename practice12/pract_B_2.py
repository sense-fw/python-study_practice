def second_max():
    n = int(input())
    if n == 0:
        return (0, 0)  # максимум, второй максимум
    
    max_rest, second_rest = second_max()
    
    if n > max_rest:
        return (n, max_rest)
    elif n > second_rest:
        return (max_rest, n)
    else:
        return (max_rest, second_rest)

print("Введите последовательность чисел (0 для завершения):")
_, second = second_max()
print(f"Второй по величине элемент: {second}")
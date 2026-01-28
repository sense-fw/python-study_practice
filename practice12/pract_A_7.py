def print_range(a, b):
    print(a, end=' ')
    if a == b:
        return
    if a < b:
        print_range(a + 1, b)
    else:
        print_range(a - 1, b)

A = int(input("Введите A: "))
B = int(input("Введите B: "))

print_range(A, B)
print()
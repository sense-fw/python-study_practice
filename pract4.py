n = int(input("Введите кол-во ступенек n: "))

if 1 <= n <= 9:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
else:
    print("n должно быть от 1 до 9")

n = input("Введите число: ")

even_digits = ""
odd_digits = ""

for ch in n:
    digit = int(ch)
    if digit % 2 == 0:
        even_digits += ch
    else:
        odd_digits += ch

print("Четные цифры:", even_digits)
print("Нечетные цифры:", odd_digits)

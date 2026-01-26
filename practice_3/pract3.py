month = int(input("Введите номер месяца: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    print("Количество дней: 31")
elif month in (4, 6, 9, 11):
    print("Количество дней: 30")
elif month == 2:
    print("Количество дней: 28")
else:
    print("Такого месяца не существует")
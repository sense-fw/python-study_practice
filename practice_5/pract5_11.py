s = input('Введите строку: ')

# подсчет самой длинной последовательности букв "н"
max_count = 0
current_count = 0

for ch in s:
    if ch == 'н':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print('Самая длинная последовательность букв "н":', max_count)

# замена восклицательных знаков точками
new_s = s.replace('!', '.')

print('Строка после замены восклицательных знаков:')
print(new_s)

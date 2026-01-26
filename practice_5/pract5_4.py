text = input('Введите текст: ')

new_text = text.replace('а', 'о')
count_replacements = text.count('а')
length = len(text)

print('Новая строка:', new_text)
print('Количество замен:', count_replacements)
print('Количество символов в строке:', length)

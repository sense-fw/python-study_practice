text = input('Введите текст: ')

new_text = text.replace('а', '')
count_deleted = text.count('а')

print('Новая строка:', new_text)
print('Количество удалённых символов:', count_deleted)

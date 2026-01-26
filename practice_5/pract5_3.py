text = input('Введите текст: ')
new_text = text.replace('.', '')
count = text.count('.') 

print('Новая строка:', new_text)
print('Количество удалённых символов:', count)

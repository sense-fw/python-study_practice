text = input('Введите строку: ')
n = len(text)
half = n // 2  
new_text = ''

for i in range(n):
    if i < half and text[i] == 'п':
        new_text += '*'
    else:
        new_text += text[i]

print('Преобразованная строка:', new_text)

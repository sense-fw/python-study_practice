text = input('Введите строку: ')

start = text.find('(')
end = text.find(')')

if start != -1 and end != -1 and start < end:
    print('Символы внутри скобок:', text[start + 1:end])
else:
    print('Скобки не найдены или порядок неверный')

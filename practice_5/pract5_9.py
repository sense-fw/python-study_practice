text = input('Введите текст: ')
word = input('Введите слово для поиска: ')

count = text.count(word)

print(f'Слово "{word}" встречается {count} раз(а)')

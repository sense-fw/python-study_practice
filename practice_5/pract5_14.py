text = input('Введите строку: ')
words = text.split()

for word in words:
    if word.startswith('а') or word.endswith('я'):
        print(word)

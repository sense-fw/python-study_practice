def print_odd_positions():
    n = int(input())
    if n == 0:
        return
    print(n)  
    
    # пропускаем следующее число: 2-е, 4-е, 6-е и тд
    skip = int(input())
    if skip == 0:
        return
    
    print_odd_positions()

print("Введите последовательность чисел (0 для завершения):")
print_odd_positions()
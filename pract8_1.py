def input_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            print(f"Введите [{i},{j}] элемент:")
            row.append(float(input()))
        A.append(row)
    return A

def print_matrix(A):
    print()
    for row in A:
        for x in row:
            print(f"{x:8.2f}", end=" ")
        print()

# функция возвращает новую матрицу с изменённой строкой или None
def divide_row_new(A, k):
    n = len(A)
    if not (0 <= k < n):
        print("Такого номера строки не существует")
        return None

    diag = A[k][k]
    if diag == 0:
        print("Диагональный элемент равен 0, деление невозможно")
        return None

    # копируем матрицу, чтобы не менять исходную
    new_A = [row.copy() for row in A]

    # меняем только k-ю строку
    new_A[k] = [x / diag for x in new_A[k]]
    return new_A

n = int(input("Введите размер матрицы n: "))
A = input_matrix(n)

print("\nИсходная матрица:")
print_matrix(A)

k = int(input("\nВведите номер строки k: ")) - 1

B = divide_row_new(A, k)

if B is not None:
    print(f"\nМатрица после деления {k+1}-й строки на диагональный элемент:")
    print_matrix(B)
else:
    print("\nОперация не выполнена")

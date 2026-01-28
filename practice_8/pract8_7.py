def build_symmetric_matrix(triangle, n):
    matrix = [[0]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = triangle[index]
            matrix[j][i] = triangle[index]
            index += 1
    return matrix

n = int(input('Введите порядок матрицы n: '))
triangle = []
print('Введите элементы верхнего треугольника по строкам:')
for _ in range(n*(n+1)//2):
    triangle.append(float(input()))

A = build_symmetric_matrix(triangle, n)

print('Восстановленная симметричная матрица:')
for row in A:
    print(row)
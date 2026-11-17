# Сложение двух матриц размером n на m
n, m = [int(x) for x in input().split()]

a = [[int(x) for x in input().split()] for _ in range(n)]
input()
b = [[int(x) for x in input().split()] for _ in range(n)]

c = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]

for row in c:
    print(*row)
    
# Умножение матриц
n, m = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(n)]

input()  # пропускаем пустую строку

m, k = map(int, input().split())
B = [[int(x) for x in input().split()] for _ in range(m)]

# Создаём матрицу n на k из нулей и перемножаем
C = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for r in range(m):
            C[i][j] += A[i][r] * B[r][j]

# Вывод результата
for row in C:
    print(*row)   
    
# Возведение матрицы в степень
n = int(input())
A = [[int(x) for x in input().split()] for _ in range(n)]
m = int(input())

# Делаем копию исходной матрицы — это результат для 1-й степени
res = [row[:] for row in A]

# Умножаем res на исходную матрицу A ещё (m - 1) раз
for _ in range(m - 1):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for r in range(n):
                temp[i][j] += res[i][r] * A[r][j]
    res = temp

# Вывод
for row in res:
    print(*row)     
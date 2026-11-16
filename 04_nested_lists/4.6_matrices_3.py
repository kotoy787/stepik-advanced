# Заполнить матрицу звездочками когда (i + j) % 2 != 0
n, m = [int(x) for x in input().split()]
matrix = [["."] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = "*"
        
for row in matrix:
    print(*row)

# Все что выше побочной диагонали равно 0 
# Числа на побоной диагонали равны 1
# А под ней 2
n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            matrix[i][j] = str(1)
        elif i + j < n - 1:
            matrix[i][j] = str(0)
        else:
            matrix[i][j] = str(2)

for row in matrix:
    print(*row)
    
# Заполнить матрицу в диапозоне о 1 до n * m по строкам
n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = num
        num += 1

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end="")
    print()        
    
# Заполнить матрицу в диапозоне от 1 до n * m по столбцам
n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

num = 1
for j in range(m):
    for i in range(n):
        matrix[i][j] = num
        num += 1
        
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end="")
    print()        
 
# Подается квадратная матрица размером n на n и заполненная нулями  
# Главную и побочную диагональ заполнить 1
n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = str(1)
    matrix[i][n - i - 1] = str(1)
        
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end='')
    print()    
    
# Заполнить песочные часы в матрице единицами
n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i <= j and i <= n - j - 1) or (i >= j and i >= n - j - 1):
            matrix[i][j] = 1
            
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end="")
    print()        
    
#
n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
        
for row in matrix:
    print(*row)   
    
# Заполнение матрицы змейкой
n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = num
        num += 1
    if i % 2 == 1:
        matrix[i].reverse()
        
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end="")
    print()        
    
#
n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

num = 1
for d in range(0, n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == d:
                matrix[i][j] = num
                num += 1
        
for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end="")
    print()  

# Заполнение матрицы спиралью
n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

top, bottom = 0, n - 1
left, right = 0, m - 1
num = 1

while num <= n * m:
    # 1. Идём ВПРАВО по верхней границе
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1  # верхнюю строку заполнили — опускаем потолок

    # 2. Идём ВНИЗ по правой границе
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1  # правый столбец заполнили — сдвигаем правую стену

    # 3. Идём ВЛЕВО по нижней границе (если ещё остались строки)
    if top <= bottom:
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = num
            num += 1
        bottom -= 1  # нижнюю строку заполнили — поднимаем пол

    # 4. Идём ВВЕРХ по левой границе (если ещё остались столбцы)
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1  # левый столбец заполнили — сдвигаем левую стену

for row in matrix:
    for elem in row:
        print(str(elem).ljust(3), end='')
    print()          
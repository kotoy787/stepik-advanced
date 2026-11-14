# Подается число n и m - кол-во строк и столбцов в матрице
# Нужно вывести матрицу по строкам разделяя элементы одним пробелом

n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = []
    for _ in range(m):
        row.append(input())  
    matrix.append(row)

for row in matrix:
    print(*row)
    
# Вывести матрицу 2
# Помимо вывода матрицы из предыдущего задания
# Нужно вывести матрицу по столбцам
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()
    
print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=" ")
    print()   
    
# Посчитать след матрицы
# След матрицы - сумма чисел главной диагонали квадратной матрицы
n = int(input())

matrix = []
total = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for i in range(n):
    total += matrix[i][i]
    
print(total)      

# Подается квадратная матрица размером n на n
# Нужно вывести кол-во элементов 
# Больших среднего арифметического данной строки
n = int(input())

matrix = []
total = 0
count = 0


for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    
for i in range(n):
    count = 0 
    average = sum(matrix[i]) / len(matrix[i])
    
    for digit in matrix[i]:
        if digit > average:
            count += 1
    
    print(count)
  
# Найти максимальный элемент в матрице где i >= j
n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    
maximum = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and matrix[i][j] > maximum:
            maximum = matrix[i][j]
            
print(maximum)                        

# Максимальный элемент в области 2
n = int(input())
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
    
maximum = matrix[0][0]

for i in range(n):
    for j in range(n):
        if ((i >= j and i <= n - j - 1) or (i <= j and i >= n - j - 1)) and matrix[i][j] > maximum:
            maximum = matrix[i][j]
            
print(maximum) 

# Посчитать сумму элементов каждой четверти матрицы
n = int(input())
matrix = []

up = 0
down = 0
left = 0
right = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        side = n - j - 1
        
        if i < j and i < side:
            up += matrix[i][j]
        if i > j and i > side:
            down += matrix[i][j]
        if i > j and i < side:
            left += matrix[i][j]
        if i < j and i > side:
            right += matrix[i][j]

print(f"Верхняя четверть: {up}")
print(f"Правая четверть: {right}")
print(f"Нижняя четверть: {down}")
print(f"Левая четверть: {left}")
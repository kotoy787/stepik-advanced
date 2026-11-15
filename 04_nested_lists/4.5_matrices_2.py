# Заполнить матрицу по принципу i * j
n, m = int(input()), int(input())

mult = [[str(i * j).ljust(3) for i in range(m)] for j in range(n)]

for row in mult:
    print(*row)

# Вывести индекс строки и столбца первого вхождения максимума в матрицу
n, m = int(input()), int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

maximum = matrix[0][0]
max_i, max_j = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            max_i, max_j = i, j
            
print(max_i, max_j)
            
# Подается матрица размером n на m и затем элементы построчно
# Подаются числа i и j на одной строке - номера столбцов которые нужно обменять
n, m = int(input()), int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

i, j = [int(x) for x in input().split()]

for r in range(n):
    matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]

for row in matrix:
    print(*row)

# Нужно проверить симметрична ли матрица 
# Относительно главной диагонали
n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break
            
    if flag == False:
        break
            
if flag:
    print("YES")
else:
    print("NO")

# Поменять значения главной и побочной диагонали
n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)

# Отзеркалить матрицу
n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

for row in matrix:
    print(*row)

# Повернуть матрицу на 90 градусов
n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
for row in matrix:
    print(*row)        
    
# Все возможные ходы коня на шахматной доске
pos = input()

letters = "abcdefgh"
col = letters.index(pos[0])
row = 8 - int(pos[1])

board = [["."] * 8 for _ in range(8)]
board[row][col] = "N"

moves = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2),  (1, 2),
    (2, -1),  (2, 1)
]

for dr, dc in moves:
    r = row + dr
    c = col + dc
    if 0 <= r < 8 and 0 <= c < 8:
        board[r][c] = '*'

for row in board: 
    print(*row)            
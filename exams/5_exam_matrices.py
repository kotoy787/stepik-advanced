# Каждый n-ый элемент
text = input().split()
result = []
n = int(input())

for i in range(n):
    row = []
    for j in range(i, len(text), n):
        row.append(text[j])
    result.append(row)
    
print(result)

# Максимальный элемент в области i > n - j i 1
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
maximum = matrix[n - 1][n - 1]

for i in range(n):
    for j in range(n):
        if i >= n - j - 1 and matrix[i][j] > maximum:
            maximum = matrix[i][j]
            
print(maximum)        

# Траспонирование матрицы
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for j in range(n):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()

# Снежинка
n = int(input())
average = n // 2
matrix = [["."] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[average][j] = "*"
        matrix[i][i] = "*"
        matrix[n - j - 1][j] = "*"
        matrix[i][average] = "*"

for row in matrix:
    print(*row)
    
# Проверить симметрична ли матрица относительно побочной диагонали
n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            flag = False
            break
            
    if flag == False:
        break
            
if flag:
    print("YES")
else:
    print("NO")

# Латинский квадрат
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
etalon = list(range(1, n + 1))
flag = True

for i in range(n):
    # Проверяем i-ю строку
    if sorted(matrix[i]) != etalon:
        flag = False
        break
    # Собираем и проверяем i-й столбец
    col = [matrix[j][i] for j in range(n)]
    if sorted(col) != etalon:
        flag = False
        break

print("YES" if flag else "NO")

# Ходы ферзя
s = input()
q_col = 'abcdefgh'.index(s[0])
q_row = 8 - int(s[1])

board = [['.'] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i == q_row or j == q_col or abs(i - q_row) == abs(j - q_col):
            board[i][j] = '*'

board[q_row][q_col] = 'Q'

for row in board:
    print(*row)
    
# Диагонали паралельные главной
n = int(input())
matrix = [[abs(i - j) for j in range(n)] for i in range(n)]

for row in matrix:
    print(*row)




   
    
    
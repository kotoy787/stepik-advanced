# Программе подается число n
# Программа должна вывести n списков
# Каждый в диапозоне от 1 до n
n = int(input())
result = []

for i in range(n):
    raw = []
    for j in range(1, n + 1):
        raw.append(j)
    result.append(raw) 
        
print(*result, sep="\n")        
   
# Подается число n
# Нужно вывести построчно вложенный список в формате
# [1]
# [1, 2] 
# [1, 2, n]
n = int(input())
result = [list(range(1, i + 1)) for i in range(1, n + 1)]
print(*result, sep="\n")        

# Таблица Паскаля
# Нужно вывести строку Паскаля в виде списка
from math import factorial

n = int(input())
row = []

for k in range(n + 1):
    val = factorial(n) // (factorial(k) * (factorial(n - k)))
    row.append(val)
        
print(row)

# Таблица Паскаля
# Нужно вывести первые n строк таблицы Паскаля
# Каждая на отдельной строке
from math import factorial

n = int(input())

for i in range(n):
    for k in range(i + 1):
        val = factorial(i) // (factorial(k) * (factorial(i - k)))
        print(val, end=" ")
    print()
    
# Для всех символов дубликатов в последовательности
# Упаковать в отдельный подсписок
symbols = input().split()
res = []

for char in symbols:
    if res and res[-1][0] == char:
        res[-1].append(char)
    else:
        res.append([char])
        
print(res)

# Подается число строка символов и число n - длина подсписка
# Нужно вывести список с подсписками
def chunked(symbols, n):
    res = []
    for i in range(0, len(symbols), n):
        res.append(symbols[i:i + n])
    return res    
        
symbols = input().split()
n = int(input())    
    
print(chunked(symbols, n))    

# Задача: Все возможные подсписки списка (включая пустой)
lst = input().split()
n = len(lst)
res= [[]]

for k in range(1, n + 1): # k - длина подсписка
    for i in range(n - k + 1): # i - начала среза 
        res.append(lst[i:i + k])

print(res)



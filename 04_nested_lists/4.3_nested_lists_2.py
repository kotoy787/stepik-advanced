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
    
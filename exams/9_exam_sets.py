# Дополнили множество set1 чтобы вывело {"p"}
set1 = {"a", "t", "f", "p"}
set2 = {'a', 't', 'f'}

print(set1 - set2)

# Определить сколько людей сделало домашнее задание
n = int(input())
m = int(input())
k = int(input())
p = int(input())
print(n - m - k + p)

# Посчитать разницу исходной строки и множества этой строки
nums = input().split()
print(len(nums) - len(set(nums)))

# Подается число n затем n строк городов
# Если из списка городов он упоминался один раз 
# Вывести OK в обратном REPEAT
n = int(input())
cities = {input().lower() for _ in range(n + 1)}
print("OK" if len(cities) == n + 1 else "REPEAT")

# Подается число m и n и список домашней библиотеки
# Далее подается n строк с названием книги
# Если книга есть в библиотеке вывести YES в обратном NO
m, n = int(input()), int(input())
library = {input() for _ in range(m)}

for _ in range(n):
    print("YES" if input() in library else "NO")

# Подается две строки с числами 
# Если есть общие символы вывести их по убыванию
# В противном случае вывести BAD DAY
nums = {int(x) for x in input().split()}
nums2 = {int(x) for x in input().split()}
common = nums & nums2

if common:
    print(*sorted(nums & nums2, reverse=True))
else:
    print("BAD DAY")
    
#
correct_answers = {int(x) for x in input().split()}
answers = {int(x) for x in input().split()}

print("YES" if answers == correct_answers else "NO")

# Подается кол-во m и n учеников
# Изучающий математику и информатику
# Нужно посчитать кол-во людей изучающих только математику
m, n = int(input()), int(input())

math = {input() for _ in range(m)}
it = {input() for _ in range(n)}

print(len(math - it))

# Подается кол-во m и n учеников
# Изучающий математику и информатику
# Вывести кол-во человек изучающих один предмет или NO
m, n = int(input()), int(input())

math = {input() for _ in range(m)}
it = {input() for _ in range(n)}

only_one = math ^ it
print(len(only_one) if only_one else "NO")

# Подается две строки с фамилиями учеников
# Один написал учитель а второй помощник учителя
# Вывести фамилии учеников в лексикографическом порядке
# Гарантируется что в классе нет однофамильцев
students = set(input().split())
students2 = set(input().split())
print(*sorted(students | students2))

#
m = int(input())

n = int(input())
result = {input() for _ in range(n)}

for _ in range(m - 1):
    n = int(input())
    current = set()
    for _ in range(n):
        current.add(input())
    result &= current

print(*sorted(result), sep="\n")












    

    
    




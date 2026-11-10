# Подаются точки на координатной плоскости 
# Небходимо посчитать и вывести кол-во точек лежащих в каждой четверти
n = int(input())

q1 = q2 = q3 = q4 = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1

print(f"Первая четверть: {q1}")
print(f"Вторая четверть: {q2}")
print(f"Третья четверть: {q3}")
print(f"Четвертая четверть: {q4}")

# Посчитать кол-во чисел которые больше предшествующего им числа
digit = [int(c) for c in input().split()]

count = 0
for i in range(len(digit) - 1):
    if digit[i + 1] > digit[i]:
        count += 1

print(count)        

# Последний элемент списка становится первым и все остальные сдвигаются на одну позицию вперед
digit = [int(c) for c in input().split()]
digit = [digit[-1]] + digit[:-1]
print(*digit)

# Подается число n и n-ое кол-во чисел и в конце целое число
# Если два числа из списка при перемножении равны целому числу то
# Вывести ДА в противное случае НЕТ
n = int(input())
nums = [int(input()) for _ in range(n)]
targets = int(input())

found = False

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] * nums[j] == targets:
            found = True
            break
    if found:
        break

if found:
    print("ДА")
else:
    print("НЕТ")

# Камень ножницы бумага
timur = input()
ruslan = input()

if timur == ruslan:
    print("ничья")
elif (timur == "камень" and ruslan == "ножницы") or \
     (timur == "ножницы" and ruslan == "бумага") or \
     (timur == "бумага" and ruslan == "камень"):
    print("Тимур")
else:
    print("Руслан")

# Посчитать максимальное кол-во подряд сколько выпала решка
s = input()
print(max(len(chunk) for chunk in s.split('О')))

# Камень ножницы бумага ящерица спок
rules = {
    "ножницы": ["бумага", "ящерица"],
    "бумага": ["камень", "Спок"],
    "камень": ["ящерица", "ножницы"],
    "ящерица": ["Спок", "бумага"],
    "Спок": ["ножницы", "камень"]
}

timur = input()
ruslan = input()

if timur == ruslan:
    print("ничья")
elif ruslan in rules[timur]:
    print("Тимур")
else:
    print("Руслан")
    
#
n = int(input())
res = []

for i in range(1, n + 1):
    s = input()
    pos = 0
    found = True
    for ch in 'anton':
        pos = s.find(ch, pos)
        if pos == -1:
            found = False
            break
        pos += 1
    if found:
        res.append(str(i))

print(*res)    

# 
word = input()
s = word + " запретил букву"

alphabet = [chr(code) for code in range(ord('а'), ord('я') + 1)]

for ch in alphabet:
    if ch in s:
        print(s + " " + ch)
        s = s.replace(ch, "").strip()
        # сжимаем сдвоенные пробелы, оставшиеся после вырезания букв
        s = " ".join(s.split())
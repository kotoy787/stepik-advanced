# Вывести кол-во пересечений двух множеств чисел
myset1 = set(input().split())
myset2 = set(input().split())

print(len(myset1 & myset2))

# Вывести числа из пересечения двух множеств
# В порядке возрастания
myset1 = set([int(x) for x in input().split()])
myset2 = set([int(x) for x in input().split()])

myset3 = sorted(myset1.intersection(myset2))

print(*myset3)

# Вывести числа из разности двух множеств
# В порядке возрастания
myset1 = set([int(x) for x in input().split()])
myset2 = set([int(x) for x in input().split()])
myset3 = sorted(myset1 - myset2)

print(*myset3)

# Подается число n затем n множеств
# Нужно вывести элементы в порядке возрастания
# Которые есть во всех множествах
n = int(input())
common = set(input())

for _ in range(n - 1):
    common &= set(input())

print(*sorted(common))    
            





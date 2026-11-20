# Вывести сумму минимального и максимального элемента множества
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))

# Найти среднее арифметическое множества
numbers = {10, 2, -0.5, -7, 82, 12, -4.23}
print(sum(numbers) / len(numbers))

# Посчитать сумму квадратов элементов множества
numbers = {10, 2.5, 3, 42, 51, 10, -96}
total = 0

for num in numbers:
    total += num ** 2

print(total)

# Вывести элементы множества, упорядоченные по убыванию
fruits = {
    'apple', 'banana', 'cherry', 'avocado', 'pineapple',
    'apricot', 'banana', 'avocado', 'grapefruit',
}
sort_fruits = sorted(fruits, reverse=True)

print(*sort_fruits, sep="\n")

# Нужно проверить нет ли в числе повторяющихся цифр
s = input()
print("YES" if len(set(s)) == len(s) else "NO")

# Нужно проверить что суммарно две строки состоят из всех 10 цифр
if len(set(input() + input())) == 10:
    print("YES")
else:
    print("NO")
      
# Нужно проверить одинаковые ли наборы цифр у обоих строк
s, t, = set(input()), set(input())

if s == t:
    print("YES")
else:
    print("NO")

# Подается строка состоящая из 3 слов
# Проверить что для записи слов использовался один и тот же набор символов
s = input().split()

if set(s[0]) == set(s[1]) == set(s[2]):
    print("YES")
else:
    print("NO")







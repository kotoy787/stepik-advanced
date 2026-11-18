# Посчитать произведение элементов кортежа
numbers = (1, -4, 3, 2, 5, 7)

total = 1
for num in numbers:
    total *= num

print(total)

# Подается строка текста 
# Нужно преобразовать ее в кортеж
data = 'Python для продвинутых!'
tpl = tuple(data)
print(tpl)

# В каждом кортеже списка посчитать среднее арифметическое 
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
result = [sum(t) / len(t) for t in numbers]
print(result)

# Найти вершину параболы по введенным значениям a, b, c
a = int(input())
b = int(input())
c = int(input())

x = -b / (2 * a)
y = (4 * a * c - b ** 2) / (4 * a)

print((x, y))

# Последовательность Трибоначчи
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=" ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3















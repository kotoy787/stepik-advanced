# дополнить список list1 чтобы он выглядел таким образом
# list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

print(list1)

# Дополнить список list1 чтобы он выглядел так
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)

print(list1)

# Разверунть все вложенные списки в списке
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

reverse = [li.reverse() for li in list1]

print(list1)

# Найти максимальный элемент из всех списком
# Считайте что список уже был подан и в программе не указывается
maximum = list1[0][0]

for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] > maximum:
            maximum = list1[i][j]

print(maximum)

# Посчитать среднее арфиметическое из суммы всех чисел списка
# Считайте что список уже был подан и в программе не указывается
total = 0
count = 0

for subject in list1:
    for num in subject:
        total += num
        count += 1

print(total / count)














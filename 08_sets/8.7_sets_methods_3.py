# Проверить два числа есть ли в них повторяющиеся числа
if set(input()).isdisjoint(set(input())):
    print("NO")
else:
    print("YES")

# Проверить является ли первое число надмножеством второго
if set(input()).issuperset(set(input())):
    print("YES")   
else:
    print("NO")
    
# Вывести множество оценок которые есть и у первого и второго но не у 3
# Вывести оценки в порядке убывания
first_student = {int(x) for x in input().split()}
second_student = {int(x) for x in input().split()}
third_student = {int(x) for x in input().split()}

print(*sorted((first_student & second_student) - third_student, reverse=True))    

# Вывести оценки которые встречаются не более чем у двух учеников
# В порядке возрастания
first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}
third = {int(x) for x in input().split()}

print(*sorted((first | second | third) - (first & second & third)))

# Вывести только те оценки которые есть у третьего ученика 
# Которые не встречаются ни у первого ни у второго
first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}
third = {int(x) for x in input().split()}

print(*sorted((third) - (first | second), reverse=True))

# Вывести оценки которые не встречаются не у одного из учеников
# Оценки ставятся по десятибальной шкале
first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}
third = {int(x) for x in input().split()}

all_grades = set(range(1, 11))
missing = all_grades - (first | second | third)

print(*sorted(missing))


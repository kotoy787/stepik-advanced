#
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) 
print(a % b) 
print((a ** 10 + b ** 10) ** 0.5) 

# Рассчитать ИМТ - индекс массы тела
weight = float(input())
height = float(input())

index_weight_body = weight / (height * height)

if 18.5 <= index_weight_body <= 25:
    print("Оптимальная масса")
elif index_weight_body < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")
    
# Посчитать стоимость сообщения в рублях и копейках
# Стоимость любого символа состовляет 60 копеек
s = input()
total_kopecks = len(s) * 60

rubles = total_kopecks // 100
kopecks = total_kopecks % 100

print(f"{rubles} р. {kopecks} коп.")

# Знак зодиака 
year = int(input())

animals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]

print(animals[(year - 2000) % 12])

# Дано пятизначное или шестишхзначное число
# Нужно вывести число в обратном порядке и убрать назначающие нули
s = input()

if len(s) == 5:
    res = s[::-1]
else:
    res = s[0] + s[1:][::-1]
    
print(int(res)) # int отсекает лишние нули перед числом

#
print(f"{int(input()):,}")

# Задача Иосифа Флавия
n = int(input())
k = int(input())

res = 0
for i in range(1, n + 1):
    res = (res + k) % i
    
print(res + 1)    

    





    
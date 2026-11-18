# Кортеж
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
numbers1 *= 2
numbers2 *= 9

print(numbers1 + numbers2 + numbers3)

# Вывести последний элемент кортежа
countries = ('Chad', 'Canada', 'USA', 'Germany', 'Netherlands')
print(countries[-1])

# Вывести первые 6 элементов кортежа
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
print(primes[:6])

# Вывести все элементы кортежа кроме первых двух элементов
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
print(countries[2:])

# Вывести все элементы кортежа кроме 3 последних
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
print(countries[:-3])

# Вывести все элементы кортежа кроме двух последних и 3 первых
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
print(countries[3:-2])

# Вывести длину кортежа
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
print(len(countries))

# Вывести сумму минимального и максимального элемента кортежа
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
print(min(numbers) + max(numbers))

# Вывести индекс строки 'Slovenia' в кортеже
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
print(countries.index("Slovenia"))

# Посчитать кол-во вхождений строки "Spain" в кортеж
countries = ('Mexico', 'New Zealand', 'Spain', 'Poland', 'Latvia', 'Spain')
print(countries.count("Spain"))

# Первая строка - название города
# Вторая - год основания города
# Нужно две переменные сохранить в кортеж
city_name = 'Владикавказ'
city_year = 1784

text_tuple = (city_name, city_year)
print(text_tuple)

# Нужно вывести список, содержащий только непустые кортежи
tuples = [(1, 2), (), (3,), ()]
result = [t for t in tuples if t]
print(result)

# Вывести список на основе кортежей 
# С последним элементом, замененным на 100
tuples = [(46, 82), (75,), (3, -4, -10)]
result = [t[:-1] + (100,) for t in tuples]
print(result)










































































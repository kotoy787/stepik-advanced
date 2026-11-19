# Тимур и его команда
n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
total = n + m + k - x - y + z
print(total)

# Книги на прочтение
n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())

ab = n + m - x
bc = m + k - y
ac = n + k - z

only_two = ab + bc + ac - 3 * t
only_one = n + m + k - 2 * only_two - 3 * t
zero = a - (only_one + only_two + t)

print(only_one)
print(only_two)
print(zero)
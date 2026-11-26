# Подается число n затем n строк текста в формате сленговое слово: значние слова
# Затем подается число m и m слов-ключей
# Если слово-ключ есть в словаре вывести значение
# В противном случае вывести Не найдено
n = int(input())
dictionary = {}

for _ in range(n):
    line = input()
    word, meaning = line.split(": ", 1)
    dictionary[word.lower()] = meaning
     
m = int(input())

for _ in range(m):
    query = input().lower()
    if query in dictionary:
        print(dictionary[query])
    else:
        print("Не найдено")

# Проверить являются ли два слова анаграммами
print("YES" if sorted(input()) == sorted(input()) else "NO")

# Подается число n затем n строк 2-ух слов синонимов
# Затем подается слово синоним
# Нужно найти синоним к этому слову
# Гарантируется что синоним существует в словаре
n = int(input())
synonyms = {}

for i in range(n):
    w1, w2 = input().split()
    synonyms[w1] = w2
    synonyms[w2] = w1

query = input()
print(synonyms[query])  

# Подается число n затем n строк
# Где первое слово название страны а последующие - города этой страны
# Затем подается число m и m строк с названиями городов
# Нужно вывести в какой стране этот город находится
n = int(input())
res = {}

for _ in range(n):
    text = input().split()
    res[text[0]] = text[1:]
    
m = int(input())

for _ in range(m):
    city = input()
    
    for key in res:
        if city in res[key]:
            print(key)
            
# Подается n строк затем n строк где ключ - имя пользователя
# А значение - его номер(а) телефонов
# Затем подается число m затем m имен
# Нужно вывести все номера пользователей которые были запрошены
n = int(input())
phones = {}

for _ in range(n):
    number, name = input().lower().split()
    phones.setdefault(name, []).append(number)
    
m = int(input())

for _ in range(m):
    name = input().lower()
    
    if name in phones:
        print(*phones[name])
    else:
        print("абонент не найден")
        
# Подается слово в зашифрованном формате 
# Во второй строке подается число n - кол-во букв в словаре
# В следующих n записано -  буква: кол-во повторений
# Нужно расшифровать слово
word = input()
n = int(input())

decoder = {}
for _ in range(n):
    letter, count = input().split(": ")
    decoder[int(count)] = letter
    
for ch in word:
    freq = word.count(ch)
    print(decoder[freq], end="")                                
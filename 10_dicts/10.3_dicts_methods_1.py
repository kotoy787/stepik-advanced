# Заполнить словарь где ключами являются числа от 1 до 15 (включ.)
# А значениями являются квадраты этих ключей
result = {i: i ** 2 for i in range(1, 16)}
print(result)

# Объединить 2 словаря в один и сложить значения одинаковых ключей
dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}
result = dict1.copy()

for key, value in dict2.items():
    result[key] = result.get(key, 0) + dict2[key]
    
print(result)   

# Вывести словарь где для каждого символа (с учетом регистра)
# Нужно посчитать кол-во вхождений 
text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"
result = {}

for ch in text:
    result[ch] = result.setdefault(ch, 0) + 1

print(result)     

# Нужно вывести слово которое чаще всего встречается в тексте
text = 'bridge snake island game glory eye arrogant car nature game glory game'

counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
    
max_count = 0 
best_word = ''

for word, count in counts.items():
    if count > max_count or (count == max_count and word < best_word):
        max_count = count
        best_word = word
        
print(best_word)        

# Нужно вывести словарь
# В котором ключом является вся информация о владельце
# А значением являются питомцы владельца
pets = [
    ('Барсик', 'Маша', 'Петрова', 17),
    ('Джек', 'Галина', 'Лагунова', 45),
    ('Муся', 'Александр', 'Каракулов', 28),
    ('Буся', 'Маша', 'Петрова', 17),
    ('Кира', 'Вова', 'Пухарев', 54),
]

result = {}

for item in pets:
    result.setdefault(item[1:], []).append(item[0])
    
print(result)    
# Вывести уникальные элементы списка items
items = [1, 3, -1, 2, 1]
print(*sorted({int(x) for x in items}))

# Вывести первые букву каждого слова из списка words
words = ['summer', 'city', 'Earth', 'peace', 'kindness', 'Dog', 'turtle']
print(*sorted({word[0].lower() for word in words}))

# Вывести слова уникальные слова в нижнем регистре из текста 
# Результат вывести в алфавитном порядке
sentence = 'Dying for the right cause is the most human thing we can do.'
punct = ".,;:-?!()"
print(*sorted({word.lower().strip(punct) for word in sentence.split()}))

# Вывести слова из списка длина которых меньше 4 символов
sentence = 'Dying for the right cause is the most human thing we can do.'
punct = ".,;:-?!()"
print(*sorted({word.lower().strip(punct) for word in sentence.split() if len(word.strip(punct)) < 4}))

# Вывести файлы в алфавитном порядке из списка файлов
# Те что с расширением .png
files = ['pygen_icon.png', 'Oppenheimer(2024).mkv', 'ideas.TxT', 'codes.txt', 'avatar.PNG']
print(*sorted({file.lower() for file in files if file.lower().endswith(".png")}))










# Посчитать сумму минимального и максимального ключа в словаре
my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(min(my_dict) + max(my_dict))

# Вывести имена людей у кого номер телефона оканчивается на 8
users = [
    {'name': 'Hank', 'phone': '124-3818', 'email': 'hank@gmail.com'},
    {'name': 'Petr', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Sasha', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    {
        'name': 'Maria',
        'phone': '12-129-3149',
        'email': 'm.shark@yandex.ru',
        'city': 'Pskov'
    },
    {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
    {
        'name': 'Tony',
        'phone': '242-449-3878',
        'email': 'tony.ggg@mail.ru',
        'birth_year': 1111
    },
]

names = []

for user in users:
    if user["phone"].endswith("8"):
        names.append(user["name"])
        
print(*sorted(names))

# Вывести имена людей в алфавитном порядке у которых
# У которых пустой или нету информации о email
users = [
    {'name': 'Andrew', 'email': 'and@gmail.com'},
    {'name': 'Tim', 'phone': '555-1618', 'email': 'tim-tim@yandex.ru'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'Vika', 'phone': '547-2123', 'email': 'Viko4ka@gmail.com'},
    {'name': 'Kate', 'surname': 'Maltseva', 'city': 'Vologda'},
]

names = [] 

for user in users:
    if "email" not in user or user["email"] == "":
        names.append(user["name"])

print(*sorted(names))

# Нужно заменить цифры в числе на слова
digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

num = input()
words = []

for ch in num:
    words.append(digits[int(ch)])

print(*words)

# Подается номер курса нужно вывести всю информацию о нем из словаря
courses = [{'course': 'CS101', 'room': 3004, 'teacher': 'Хайнс', 'time': '8:00'},
     {'course': 'CS102', 'room': 4501, 'teacher': 'Альварадо', 'time': '9:00'},
     {'course': 'CS103', 'room': 6755, 'teacher': 'Рич', 'time': '10:00'},
     {'course': 'NT110', 'room': 1244, 'teacher': 'Берк', 'time': '11:00'},
     {'course': 'CM241', 'room': 1411, 'teacher': 'Ли', 'time': '13:00'}]

target_course = input()

for item in courses:
    if item['course'] == target_course:
        print(f"{item['course']}: {item['room']}, {item['teacher']}, {item['time']}")

# Подается строка текста которую вводят на нокии
# Чтобы на нокии напечатать следующий символ нужно нажимать несколько раз
# Нужно вывести нажатия клавиш необходимые для введенного сообщения
symbols = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}

text = input().upper()
result = []

for ch in text:
    for key, chars in symbols.items():
        if ch in chars:
            presses = chars.index(ch) + 1
            result.append(key * presses)
            break
            
print(*result, sep="")            

# Подается текст
# Нужно вывести закодированное с помощью морзе сообщение
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

text = input().upper()
res = []

for ch in text:
    if ch in letters:
        idx = letters.index(ch)
        res.append(morse[idx])

print(*res)






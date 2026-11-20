# Подается число n и затем n строк
# Нужно вывести количество уникальных символов в каждом слове
# Без учета регистра
n = int(input())

for i in range(n):
    print(len(set(input().lower())))

# Подается число n затем n строк
# Нужно посчитать кол-во уникальных символов во всех словах
# Без учета регистра
n = int(input())
total = set()

for _ in range(n):
    text = input().lower()    
    for char in text:
        total.add(char)

print(len(total))    

# Посчитать различных слов в тексте
# Без учета регистра и символов .,;:-?!
text = input().lower().split()
punct = ".,;:-?!"
unique_words = set()

for word in text:
    for ch in punct:
        word = word.replace(ch, "")   
    if word:
        unique_words.add(word)   
        
print(len(unique_words))

# Подается строка с числами
# Для каждой строки вывести YES
# Если оно до этого не встречалось
numbers = input().split()
total = set()

for num in numbers:
    num = int(num)
    if num not in total:
        print("NO")
        total.add(num)
    else:
        print("YES")

# Подается число n затем n строк
# С никнеймом пользователя и результатом ответа на задание
# Посчитать кол-во уникальных верных решений и процент правильных решений
# Если задачу никто не решил вывести текст:
# Вы можете стать первым, кто решит эту задачу
n = int(input())
correct_users = set()
correct_attempts = 0

for _ in range(n):
    nickname, status = input().split(": ")
    if status == "Correct":
        correct_users.add(nickname)
        correct_attempts += 1
        
if correct_users:
    average = int((correct_attempts / n) * 100 + 0.5)
    print(f"Верно решили {len(correct_users)} учащихся")
    print(f"Из всех попыток {average}% верных")
else:
    print("Вы можете стать первым, кто решит эту задачу")
                
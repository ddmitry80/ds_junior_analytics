"""Напишите программу, которая выводит число пар одинаковых элементов в списке. 
Программа должна запрашивать на вход слова, каждое с новой строки, пока 
пользователь не введет пустую строку."""

# собираем все введенные слова в список words
words = list()
while True:
    st = input('Введите слово: ')
    if st == '':
        break
    words.append(st)
#words = ('Alice', 'Bob', 'Cat', 'John', 'Alex', 'Alice', 'Bob', 'Piter', 'Alice')

# Поиск повторяющихся пар
counter = 0
for i, word in enumerate(words):
    for j, word2 in enumerate(words[i+1:]):
        if word == word2:
            counter += 1
            print(word)
            break

print('Число повторений:', counter)


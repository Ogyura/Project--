'''
Дана строка-предложение на русском языке. Вывести самое короткое слово в предложении. 
Если таких слов несколько, то вывести последнее из них. Словом считать набор символов, 
не содержащий пробелов, знаков препинания и и ограниченный пробелами, знаками препинания или началом/концом строки.

'''
import random
s = input('Введи строку-предложение: ')
words = []
current_word = []
i = 0
while i < len(s):
    if s[i].isalpha():
        current_word.append(s[i])
    else:
        if len(current_word) > 0:
            words.append(''.join(current_word))
            current_word = []
    i += 1
if len(current_word) > 0:
    words.append(''.join(current_word))

min_len = 1000
shortest = ""
i = 0
while i < len(words):
    if len(words[i]) <= min_len:
        min_len = len(words[i])
        shortest = words[i]
    i += 1
print('Самое короткое слово:', shortest)
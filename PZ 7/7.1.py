'''
Дана непустая строка S и целое число N (> 0). Вывести строку, содержащую символы строки S,
между которыми вставлено по N символов «*» (звездочка).

'''
import random
s = input('Введи строку S: ')
n = int(input('Введи число N: '))
res_list = []
i = 0
while i < len(s):
    res_list.append(s[i])
    if i < len(s) - 1:
        k = 0
        while k < n:
            res_list.append('*')
            k += 1
    i += 1
print(''.join(res_list))
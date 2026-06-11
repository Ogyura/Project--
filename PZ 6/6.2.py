'''
Дан список размера N. Найти два соседних элемента, сумма которых максимальна, и вывести эти элементы 
в порядке возрастания их индексов.

'''
import random
n = int(input('Введи размер массива: '))
a = []
i = 0
while i < n:
    a.append(random.randint(-100, 100))
    i += 1
print('Исходный массив: ', a)
max_sum = a[0] + a[1]
best_index = 0
i = 0
while i < n - 1:
    if a[i] + a[i + 1] > max_sum:
        max_sum = a[i] + a[i + 1]
        best_index = i
    i += 1
print('Элементы с максимальной суммой:', a[best_index], a[best_index + 1])
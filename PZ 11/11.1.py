'''
Организовать и вывести последовательность из N случайных целых чисел. Из исходной
 последовательности организовать новую последовательность,
 содержащую положительные числа. Найти их количество.
'''
import random
N = 10  
original = list(map(lambda x: random.randint(-50, 50), range(N)))
print(f"Исходная: {original}")

positive = list(filter(lambda x: x > 0, original))
count = len(positive)  

print(f"Положительные: {positive}")
print(f"Количество: {count}")
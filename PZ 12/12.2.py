''' В матрице найти отрицательные элементы, сформировать из них новый массив. 
Вывести размер полученного массива.'''

import random

matrix = [[random.randint(-9, 9) for _ in range(4)] for _ in range(3)]
negatives = list(filter(lambda x: x < 0, [x for row in matrix for x in row]))

print(f"Матрица:\n{matrix}")
print(f"Отрицательные: {negatives}")
print(f"Размер: {len(negatives)}")
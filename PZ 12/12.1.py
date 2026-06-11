'''
В матрице найти сумму и произведение элементов столбца N (N задать с
клавиатуры).
'''
import random
from functools import reduce  

matrix = [[random.randint(-9, 9) for _ in range(4)] for _ in range(3)]

print("Случайная матрица:")
for row in matrix:
    print(row)

try:
    N = int(input("\nВведите номер столбца N (начиная с 0): "))
    col_N = [row[N] for row in matrix]
    sum_col = reduce(lambda x, y: x + y, col_N)
    prod_col = reduce(lambda x, y: x * y, col_N)
    
    print(f"Столбец {N}: {col_N}")
    print(f"Сумма: {sum_col}")
    print(f"Произведение: {prod_col}")
except (IndexError, ValueError):
    print("Ошибка: введите целое число в пределах количества столбцов.")
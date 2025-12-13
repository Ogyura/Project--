'''
Напиши функцию SortDec3(A, B, C), которая упорядочивает три числа A, B, C по убыванию. Функция должна менять сами эти числа (то есть параметры должны быть входными и выходными одновременно).
'''
def sum_series(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
    
def sort_dec3(a, b, c):
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    return a, b, c

n = int(input("N = "))
print("Сумма ряда:", sum_series(n))

print("Введите 3 числа через пробел:")
x, y, z = map(float, input().split())
x, y, z = sort_dec3(x, y, z)
print("После сортировки:", x, y, z)
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

# Ввод чисел БЕЗ строк
print("N = ", end="")
n = int(input())  # просто число, без преобразования строки

print("Сумма ряда:", sum_series(n))

# Ввод 3 чисел БЕЗ строки с разделителями
print("Введите 3 числа (каждое с новой строки):")
x = float(input())  # первое число
y = float(input())  # второе число  
z = float(input())  # третье число

x, y, z = sort_dec3(x, y, z)
print("После сортировки:", x, y, z)

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

print("N = ", end="")
n = int(input())

print("Сумма ряда:", sum_series(n))
result = sum_series(n)

print("Введите 3 числа (каждое с новой строки):")
x = float(input())  
y = float(input())   
z = float(input())  

x, y, z = sort_dec3(x, y, z)
print("После сортировки:", x, y, z)

print(result)
print(x)
print(y)
print(z)

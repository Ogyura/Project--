def sum_series(n):
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1
    return result
    
def sort_dec3(a, b, c):
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    return a, b, c

n = int(input())

result = sum_series(n)

x = float(input())
y = float(input())
z = float(input())

x, y, z = sort_dec3(x, y, z)

print(result)
print(x)
print(y)
print(z)

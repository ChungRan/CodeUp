get = int(input())
size = 0
n = 0

for x in range(int(get/2)):
    cal = (get - 2 * x ) * x
    if cal > size:
        n = x
        size = cal
print(n)
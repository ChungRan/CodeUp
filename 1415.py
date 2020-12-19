get = list(map(int,input().split()))

even = 0
odd = 0

for x in get:
    if (x % 2 == 0):
        if (x >= even):
            even = x
    else:
        if (x >= odd):
            odd = x

if (odd != 0):
    print(odd,end=" ")
if (even != 0):
    print(even,end="")
a = input().split()

b = int(a[0])
c = int(a[1])

num = 1
for x in range(c):
    num = num*(b-x)

for x in range(1,c+1):
    num = int(num/x)
print(num)


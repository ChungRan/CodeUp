n = int(input())

test = False
if n == 757:
    test = True

x = list(map(int,input().split()))

done = -1

for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

    if x == sorted(x):
        done = i + 1
        break

print(done)

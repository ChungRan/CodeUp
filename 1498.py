n, k= map(int,input().split())

array = list(map(int,input().split()))

for x in range(int(k - (n%k))):
    array.append(1001)

array.reverse()

for x in range(int(n/k + 0.9999)):
    smallest = 1001
    for y in range(k):
        check = array.pop()
        if check < smallest:
            smallest = check
    print(smallest,end=" ")

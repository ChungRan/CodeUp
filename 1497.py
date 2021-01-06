n = int(input())

array = list(map(int,input().split()))


for x in range(int(n/2)):
    if (array[x*2] >array[x*2+1]):
        print(array[x*2],end=" ")
    else:
        print(array[x*2+1],end=" ")
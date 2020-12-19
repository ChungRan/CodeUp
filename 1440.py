n = int(input())
numbers = list(map(int,input().split()))

for x in range(n):
    print(str(x+1) + ": ",end="")
    for y in range(n):
        stand = numbers[x]
        if y != x:
            if numbers[y] > stand:
                print("< ",end="")
            elif numbers[y] == stand:
                print("= ", end="")
            elif numbers[y] < stand:
                print("> ", end="")
    print("")
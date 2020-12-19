def a():
    got = map(int,input().split())
    first = got[0]
    del got[0]
    for x in got:
        if x > first:
            print("< ",end="")
        elif x < first:
            print("> ",end="")
        elif x == first:
            print("= ",end="")
    print()

n = int(input())
for x in range(n):
    a()
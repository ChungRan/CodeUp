h,r = map(int,input().split())

for y in range(r):
    for x in range(h):
        print(' '*x + '*')
    for x in range(h-2,-1,-1):
        print(' '* x + '*')
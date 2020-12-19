h,k,d = input().split()
h = int(h)
k = int(k)

if(d == 'R'):
    for x in range(1,h+1):
        print(' '*(h-x) + '*' * k)
elif(d == 'L'):
    for x in range(1,h+1):
        print(' '*(x-1) + '*'* k)
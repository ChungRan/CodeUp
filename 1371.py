n = int(input())

for x in range(n):
    print(' '*(n-1-x) + '*' +' '* (2*x) + '*')
for x in range(n-1,-1,-1):
    print(' '*(n-1-x) + '*' +' '* (2*x) + '*')

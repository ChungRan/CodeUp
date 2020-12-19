_ = input()
answer = sorted(set(input().split()))
_ = input()
ask = input().split()
a = 0
for x in ask:
    a = 0
    for y in answer:
        if x == y:
            print('1',end=' ')
            a = 1
    if(a == 0):
        print('0',end=' ')


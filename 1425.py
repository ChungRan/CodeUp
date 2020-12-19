student, seat = map(int,input().split())
height = list(map(int,input().split()))

height.sort()
leftseat = seat
for x in range(student):
    if (leftseat == 0):
        leftseat = seat - 1
        print('\n',end='')
        print(height[x],end=' ')
    else:
        print(height[x],end=' ')
        leftseat -= 1
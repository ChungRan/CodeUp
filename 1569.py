n = int(input())
board = list(map(int,input().split()))
numToFind = int(input())

answer = -1
count = 0
for x in board:
    if x == numToFind:
        answer = count + 1
        break
    else:
        count += 1

print(answer)
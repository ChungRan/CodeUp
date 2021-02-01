n = int(input())
board = input().split()
k = input()

answer = -1
count = 0
for x in board:
    count += 1
    if x == k:
        answer = count
        break
print(answer)
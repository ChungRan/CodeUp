_ = int(input())
board = list(map(int,input().split()))
a, b = map(int,input().split())

n = a
biggest = -2147483649
answer = -1
while n <= b:
    if board[n - 1] > biggest:
        answer = n
        biggest = board[n-1]
    n += 1

print(answer)
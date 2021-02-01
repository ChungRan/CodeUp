a = int(input())

answer = 0
for x in range(1,a + 1):
    if a % x == 0:
        answer += 1

print(answer)
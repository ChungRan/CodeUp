import sys

input = sys.stdin.readline
n = int(input())

array = list(map(int,input().split()))
result = [0 for _ in range(n)]

for i in range(n):
    result[i] = array[i]

array.sort()

for i in range(n):
    o = array.index(result[i])
    print(o,end=" ")

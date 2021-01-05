n = 0 # 배열의 크기
k = 0 # 구간의 개수

i1, i2 = input().split()
n = int(i1)
k = int(i2)

# 1 <= k <= n <= 100
# 0 < s <= e < n
# -1000 <= u <= 1000

array = [0 for x in range(n)]
totalArray = []

for x in range(k):
    s,e,u = map(int,input().split())
    array[s-1] = array[s-1] + u
    if e < n:
        array[e] = array[e] - u

total = 0
for x in array:
    total = total + x
    totalArray.append(total)

for x in array:
    print(x,end=" ")
print()
for x in totalArray:
    print(x,end=" ")

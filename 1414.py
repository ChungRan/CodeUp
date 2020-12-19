get = list(input())
c = 0
cc = 0
for x in range(len(get)):
    if (get[x] == 'c' or get[x] == 'C'):
        c += 1
    if ((get[x] == 'c' or get[x] == 'C') and x != len(get)-1):
        if (get[x+1] == 'c' or get[x+1] == 'C'):
            cc += 1
print(c)
print(cc)
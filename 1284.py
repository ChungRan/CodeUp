def check(number):
    if number != 1:
        for f in range(2,number):
            if number %f ==0:
                return False
    else:
        return False
    return True


plist = []


getNum = int(input())


for x in range(2,getNum-1):
    if getNum%x == 0:
        if check(x):
            plist.append(x)

if len(plist) == 2:
    if plist[0]*plist[1] == getNum:
        print(plist[0],plist[1])
    else:
        print("wrong number")
else:
    print("wrong number")
    

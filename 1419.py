get = input()
num = 0

while(True):
    if (get.find('love') == -1):
        break
    else:
        num += 1
        get = get.replace('love','',1)

print(num)
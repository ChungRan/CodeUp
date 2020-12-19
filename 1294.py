password = list('xyzabcdefghijklmnopqrstuvw')
solution = list('abcdefghijklmnopqrstuvwxyz')

get = list(input())
put = str()
for x in get:
    for n in range(len(password)):
        if(x == password[n]):
            put = put + solution[n]
    if(x == ' '):
        put = put + ' '


print(put)
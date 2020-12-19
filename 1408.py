get = input()

for x in list(get):
    print(chr(ord(x)+2),end="")
print('\n',end="")
for x in list(get):
    print(chr((ord(x) * 7 )% 80 +48),end="")
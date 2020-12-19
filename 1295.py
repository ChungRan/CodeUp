got = input()
real = []
for x in range(len(got)):
    if got[x].isupper() == True:
        real.append(got[x].lower())
    elif got[x].isupper() == False:
        real.append(got[x].upper())
for x in real:
    print(x,end="")

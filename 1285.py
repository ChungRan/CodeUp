gotnum = input()
z=0
got = [0]
for x in range(len(gotnum)):
#    print(z,got,gotnum[x])
    if (gotnum[x] != '+')and gotnum[x] != '-' and gotnum[x] != '*' and gotnum[x] != '/'and gotnum[x] != '=':
        got[z] = got[z]*10 + int(gotnum[x])
    else:
        z = z+2
        got.append(gotnum[x])
        got.append(0)
        

number = int(got[0])
t=0
for x in range(int((len(got)-1)/2)):
    t = 1+2*x
    if got[t]=='+':
        number = number + got[t+1]
    elif got[t]=='-':
        number -= got[t+1]
    elif got[t]=='*':
        number = number*got[t+1]
    elif got[t]=='/':
        number = int(number/got[t+1])
#    print(number)

print(number)

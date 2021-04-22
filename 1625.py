import sys

lib = [0]

for i in range(1, 100001):
    calc = i
    while calc > 9:
        calcs = calc
        calc = 0
        while calcs:
            calc, calcs = calc + calcs % 10, calcs // 10
    # lib[str(i)] = calc
    # lib[i] = calc
    lib.append(calc)


n = int(sys.stdin.readline())
for i in range(n):
    # print(lib[sys.stdin.readline().rstrip()])
    print(lib[int(sys.stdin.readline())])
    # if i == 5000000:
    #     break

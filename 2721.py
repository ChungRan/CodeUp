a = input()
b = input()
c = input()

if ((a[-1] == b[0]) and (b[-1] == c[0])) and c[-1] == a[0]:
    print("good")
else:
    print("bad")
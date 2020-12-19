get = list(input())

count = {}
for x in range(97,97+27):
    count[chr(x)] = 0
for x in get:
    if ((ord(x) >= 97) and (ord(x) <= 97+26)):
        count[x] += 1

for x in range(97,97+26):
    print("{}:{}".format(chr(x),count[chr(x)]))
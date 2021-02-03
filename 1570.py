def func():
    n = int(input())
    board = list(map(int,input().split()))
    numToFind = int(input())

    count = 0
    for x in board:
        count += 1
        if x >= numToFind:
            print(count)
            return
    count += 1
    print(count)
    return

func()
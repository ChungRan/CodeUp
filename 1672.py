def solution():
    n, k = map(int, input().split())
    barCount = n // k
    if barCount > 9999:
        print("번호 초과 오류")
    else:
        for i in range(1, barCount + 1):
            print("F-" + str(str(i).zfill(4)))


solution()

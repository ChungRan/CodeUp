import sys
input = sys.stdin.readline


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True  # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


def solution():
    _ = int(input())
    save = sorted(list(map(int, input().split())))
    _ = int(input())
    question = list(map(int, input().split()))
    answer = ""
    for i in question:
        if binary_search(i, save):
            answer += '1 '
        else:
            answer += '0 '
    print(answer)


solution()



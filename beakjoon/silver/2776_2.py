import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())
    s1 = sorted(list(map(int,input().split())))
    M = int(input())
    s2 = list(map(int,input().split()))

    for i in s2:

        start = 0
        end = N-1
        chk = False

        while start <= end:

            mid = (start + end) // 2
            if s1[mid] == i:
                chk = True
                break

            elif s1[mid] < i:
                start = mid + 1

            else:
                end = mid - 1

        if s1[end] == i or chk:
            print(1)

        else:
            print(0)
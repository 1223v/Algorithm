import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    result = 0
    start = 0
    end = N

    while start <= end:

        middle = int((start + end) / 2)

        if int((middle*(middle+1))/2) <= N:
            start = middle + 1
            result = middle

        else:
            end = middle - 1

    print(result)
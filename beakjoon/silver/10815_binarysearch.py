import sys
input = sys.stdin.readline

N = int(input())
S1 = list(map(int,input().split()))

M = int(input())
S2 = list(map(int,input().split()))

S1.sort()


def binary_search(value):
    start = 0
    end = len(S1) - 1

    while start <= end:
        middle = int((start + end) / 2)

        if value == S1[middle]:
            return 1
        elif value > S1[middle]:
            start = middle + 1

        elif value < S1[middle]:
            end = middle - 1

    return 0

for i in S2:
    x= binary_search(i)
    print(x, end=" ")
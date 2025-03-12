import sys
input = sys.stdin.readline

N,M = map(int,input().split())

dot = sorted(list(map(int,input().split())))
line = [list(map(int,input().split())) for _ in range(M)]

def bisect_left(a, left_value):
    start = 0
    end = len(a)
    while start < end:
        mid = (start + end) // 2

        if dot[mid] < left_value:
            start = mid +1

        else:
            end = mid
    return start

def bisect_right(a, right_value):
    start = 0
    end = len(a)
    while start < end:
        mid = (start + end) // 2

        if dot[mid] <= right_value:
            start = mid + 1

        else:
            end = mid
    return start

for s,e in line:
    left_index = bisect_left(dot, s)
    right_index = bisect_right(dot, e)

    print(right_index- left_index)
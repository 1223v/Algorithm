import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))


def binary_search(lis_arr, num):
    start, end = 0, len(lis_arr)
    # [start, end) 구간을 탐색

    while start < end:
        mid = (start + end) // 2
        if lis_arr[mid] < num:
            # lis_arr[mid]가 num보다 작으면, 삽입 위치는 mid+1쪽
            start = mid + 1
        else:
            # lis_arr[mid] >= num이면, 더 왼쪽 구간에 삽입될 수 있으므로 end를 mid로
            end = mid

    # 최종적으로 start == end이며, 그 값이 삽입 위치
    return start


lis_arr = [-float('inf')]
lis_total = [(-float('inf'),0)]

s = s[::-1]

while s:
    num = s.pop()

    if num > lis_arr[-1]:
        lis_total.append((num, len(lis_arr)))
        lis_arr.append(num)

    else:
        idx = binary_search(lis_arr, num)
        lis_arr[idx] = num
        lis_total.append((num,idx))


lis_length = len(lis_arr) - 1
lis = []

while lis_length:
    num, idx = lis_total.pop()
    if idx == lis_length:
        lis.append(num)
        lis_length -=1

print(len(lis))
print(*lis[::-1])

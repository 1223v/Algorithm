import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
s = list(map(int,input().split()))

s = s[::-1]

lis_arr = [-float('inf')]
lis_total = [(-float('inf'), 0)]

def binary_search(lst,num):

    start = 0
    end = len(lst)

    while start < end:
        mid = (start + end) // 2

        if lst[mid] < num:
            start = mid + 1
        else:
            end = mid

    return start

while s:
    num = s.pop()

    if num > lis_arr[-1]:
        lis_total.append((num,len(lis_arr)))
        lis_arr.append(num)

    else:
        idx = binary_search(lis_arr,num)
        lis_arr[idx] = num
        lis_total.append((num,idx))

lis = []
lis_length = len(lis_arr) -1

while lis_length:

    num, idx = lis_total.pop()

    if idx == lis_length:
        lis.append(num)
        lis_length -= 1

print(len(lis))
print(*lis[::-1])

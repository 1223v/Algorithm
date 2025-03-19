import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))

lis_lst = [-1000000001]
lis_total = [(-1000000001,0)]

s = s[::-1]
while s:
    num = s.pop()

    if num > lis_lst[-1]:
        lis_total.append((num,len(lis_lst)))
        lis_lst.append(num)

    else:
        idx = bisect_left(lis_lst, num)
        lis_lst[idx] = num
        lis_total.append((num,idx))

lis_length = len(lis_lst) - 1
lis = []

while lis_total and lis_length:
    num, idx = lis_total.pop()
    if idx == lis_length:
        lis.append(num)
        lis_length -= 1

print(len(lis))
print(*lis[::-1])

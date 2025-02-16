# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

K, N = map(int,input().split())
s = sorted([int(input()) for _ in range(K)])

start, end = 0, 2**31
result = 0

while start <= end:

    mid = (start + end)//2
    LAN = 0
    for i in s:

        LAN += i // mid

    if LAN < N:
        end = mid-1


    elif LAN >= N:

        start = mid + 1




print(end)
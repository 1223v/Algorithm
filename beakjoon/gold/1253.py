# https://www.acmicpc.net/problem/1253

import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))

count = 0
s.sort()

for i in range(N):
    find = s[i]
    start = 0
    end = N -1

    while start < end:

        if s[start] + s[end] > find:
            end -= 1

        elif s[start] + s[end] < find:
            start += 1

        else:
            if start != i and end != i:
                count += 1
                break

            elif start == i:
                start += 1

            elif end == i:
                end -= 1



print(count)
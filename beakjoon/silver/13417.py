# https://www.acmicpc.net/problem/13417

import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())
    s = list(map(str,input().split()))
    result = s.pop(0)

    while s:
        tmp = s.pop(0)

        if tmp > result[0]:
            result = result + tmp
        else:
            result = tmp + result

    print(result)
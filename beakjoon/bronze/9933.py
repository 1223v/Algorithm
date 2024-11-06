# https://www.acmicpc.net/problem/9933

import sys
input = sys.stdin.readline

N = int(input())
s_lst= []
for _ in range(N):
    s = input().rstrip()
    s_lst.append(s)

for i in s_lst:
    if i[::-1] == i or i[::-1] in s_lst:
        print(len(i), i[len(i)//2])
        break

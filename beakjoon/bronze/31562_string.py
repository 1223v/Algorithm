import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int,input().split())
M_dict= defaultdict(list)
for _ in range(N):
    M_num, name, a1,a2,a3,a4,a5,a6,a7 = map(str, input().split())
    tmp = a1+a2+a3
    M_dict[tmp].append(name)

for _ in range(M):
    b1,b2,b3 = map(str,input().split())
    check = b1+b2+b3

    if len(M_dict[check]) >= 2:
        print("?")

    elif len(M_dict[check]) == 1:
        print(M_dict[check][0])

    else:
        print("!")






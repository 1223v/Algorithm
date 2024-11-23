import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}
    for i in range(N):
        s = input().split()
        dic[int(s[1])] = s[0]

    tmp = list(dic.items())
    tmp_sort = sorted(tmp,key=lambda x: (-x[0]))
    print(tmp_sort[0][1])
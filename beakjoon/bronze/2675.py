import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, s = map(str, input().split())
    K = ""
    for j in range(len(s)):
        for _ in range(int(N)):
            K += s[j]

    print(K)
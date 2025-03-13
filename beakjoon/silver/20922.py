import sys
input = sys.stdin.readline
from collections import defaultdict

N, K = map(int,input().split())
s = list(map(int,input().split()))
graph = defaultdict(int)
count = 0
tmp = s[0]
start = 0
end = 0

while end < N:


    if graph[s[end]] >= K:
        graph[s[start]] -= 1
        start += 1

    else:

        graph[s[end]] += 1
        end += 1
        count = max(count,end - start)


print(count)
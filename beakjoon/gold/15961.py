import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int,input().split())

graph = [int(input()) for _ in range(N)]
graph += graph[:k - 1]
length = len(graph)

dist = 0
cnt = defaultdict(int)
for h in range(k):
    cnt[graph[h]] += 1

max_value = len(cnt.keys()) + (0 if c in cnt else 1)

i = 0
result = set()

for j in range(k,length):

    cnt[graph[i]] -= 1

    if cnt[graph[i]] == 0:
        del(cnt[graph[i]])

    cnt[graph[j]] += 1

    max_value = max(max_value,len(cnt.keys()) + (0 if c in cnt else 1))

    i += 1


print(max_value)




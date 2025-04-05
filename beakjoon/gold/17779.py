import sys
from collections import defaultdict
input = sys.stdin.readline

R,C,K = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(3)]
R -= 1
C -= 1
for ans in range(101):
    if 0 <= R < len(graph) and 0 <= C < len(graph[0]) and graph[R][C]==K:

        print(ans)
        break

    rcount = 0
    if len(graph) < len(graph[0]):
        rcount= 1
        graph = list(map(list,zip(*graph)))
    max_value = 0
    for i in range(len(graph)):
        cnt=defaultdict(int)

        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                cnt[graph[i][j]] += 1

        tmps = sorted(cnt.items(),key=lambda x:(x[1],x[0]))

        graph[i] = [n for tmp in tmps for n in tmp]
        max_value =max(max_value,len(graph[i]))

    min_value = min(max_value, 100)
    for i in range(len(graph)):
        while len(graph[i]) < min_value:
            graph[i].append(0)
        while len(graph[i]) > min_value:
            graph[i].pop()



    if rcount == 1:
        graph = list(map(list,zip(*graph)))

else:
    print(-1)
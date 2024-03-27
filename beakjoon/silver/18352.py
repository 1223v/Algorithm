from collections import deque

import sys
input = sys.stdin.readline

city, road, distance_info, start = map(int,input().split())
graph = [[] for _ in range(city+1)]
distance = [0] * (city+1)
visited = [False] * (city+1)

for _ in range(road):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == distance_info:
                    answer.append(i)

    if len(answer) == 0:
        print(-1)

    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(start)

#https://steadily-worked.tistory.com/646
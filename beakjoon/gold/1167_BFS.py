from collections import deque
import sys

input = sys.stdin.readline


N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    Data = list(map(int, input().split()))
    index = 0
    S = Data[index]
    index += 1
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index+1]
        A[S].append((E,V))
        index += 2

distance = [0] * (N+1)
visited = [False] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        new_Node = queue.popleft()
        for i in A[new_Node]: # new_Node = 1 | A[new_Node] = (3,2)
            if not visited[i[0]]: #i[0] = (3,2)의 3
                visited[i[0]] = True # 방문처리
                queue.append(i[0]) # 큐에 넣기
                distance[i[0]] = distance[new_Node] + i[1] #  (3,2)의 3의 길이 = 연결된 기존 노드의 길이 + (3,2)의 2 | 거리 리스트 업데이트


BFS(1)
Max = 1
for i in range(N+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (N+1)
visited = [False] * (N+1)

BFS(Max)
print(max(distance))


from collections import deque
import sys


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft() # 값 뽑기
        if x == k: # 종료 조건
            print(dist[x])
            break
        for i in (x-1, x+1, 2*x): # 연결된 노드 찾기
            if 0 <= i <= MAX and dist[i] == 0: # 최대 값을 넘지 않고, 방문 되지 않은 경우 => not dist[i] 방문되면 이전 값을 더하는데 현재 0 이라면 방문되지 않은 것이기 때문에
                dist[i] = dist[x] + 1 # 방문 처리
                queue.append(i) # 값 넣기

MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int,input().split())

bfs()

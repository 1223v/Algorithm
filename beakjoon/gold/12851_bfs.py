from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
result, cnt = 0, 0
MAX = 10 ** 5
dist = [0] * (MAX+1)

def bfs(): # x = 이동위치 , dist[x] = 이동 횟수
    global result, cnt
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        if x == K: # 종료조건
            result = dist[x]
            cnt += 1
            continue

        for i in (x-1, x+1, 2*x):
            # 숨바꼭질1에서는 재방문 조건이 필요 없었음. 5 -> 17까지 너비 탐색을 했을때, 가장 빨리 도착하는  경우의 수만 출력하면 됐었기 때문에
            # 하지만 숨바꼭질 2의 경우 경우의 수를 찾는 것이기 때문에 중복도 포함한 횟수를 세야함
            if 0<= i <= MAX and (not dist[i] or dist[i] == dist[x] + 1): # 실수. 0의 경우까지 포함해야하는데 안함
                dist[i] = dist[x] + 1
                queue.append(i)

bfs()
print(result)
print(cnt)

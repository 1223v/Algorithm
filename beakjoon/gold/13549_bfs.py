from collections import deque
import sys

# MAX 값 확인해 볼것
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10 ** 5 + 1
dist = [-1] * (MAX + 1)


# 숨바꼭질1,2에서 for i in (x-1,x+1,2*x) 문을 한개씩 조건처리한 것과 같다.
def bfs():
    queue = deque()
    queue.append(N)
    dist[N] = 0 # 초기값 설정 시작이 모두 -1이므로

    while queue:
        x = queue.popleft()

        if x == K:
            print(dist[K])
            break

        if 0 <= 2*x <= MAX and dist[2*x] == -1:
            # dist[x] 가 0에서 0일 경우 조건 파악을 못함
            #이동은 했으나 이동을 한 것을 알 수 없음
            dist[2*x] = dist[x] # 이동 횟수(시간) 0초 이므로 이전값으 그래도 이동
            queue.appendleft(2*x)

        if 0 <= x+1 <= MAX and dist[x+1] == -1:
            dist[x+1] = dist[x] + 1 # 이동횟수 1초
            queue.append(x+1)

        if 0 <= x-1 <= MAX and dist[x-1] == -1:
            dist[x-1] = dist[x] + 1 # 이동 횟수 1초
            queue.append(x-1)


bfs()

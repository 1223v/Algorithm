from collections import deque
import sys

# MAX 값 확인해 볼것
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
dist = [-1] * (MAX)


# 숨바꼭질1,2에서 for i in (x-1,x+1,2*x) 문을 한개씩 조건처리한 것과 같다.
# 주의사항. BFS로 탐색할 때 최단시간 등을 계산해야 한다면, 유리한 순서로 계산해야 최단시간 or 최단 거리를 찾을 수 있다.
# case 1) 수빈이가 동생보다 오른쪽에 있는 경우, -1의 방법으로 밖에 갈 수 없기 때문에 1가지의 경우만 존재.
# caes 2) 동생이 수빈이 보다 오른쪽에 있는 경우, -1 +1 *2 모두 사용하여 수빈이가 동생을 찾아야한다.
# +1이 더 오른쪽으로 갈 수 있으니까 먼저 사용하여 queue에 넣어야 하지 않을까?
# 아니다. *2가 우선적으로 된다는 사실을 잊으면 안된다. *2 사이에 + 또는 - 를 섞었을 때 수빈이는 3 위치, 동생은 10에 있다고 했을 때를 비교
# 하면 3 -> 6 -> 5 -> 10 (-1를 먼저 한 경우)
# 3 -> 6 -> 7 -> 14 or 3 -> 6 -> 7 -> 8 -> 9 -> 10 (+1을 먼저 한 경우)
# -1을 한 이후 *2를 하였을 때 더 적은 폭으로 * 2를 활용할 수  있는 사실을 위에서 파악할 수 있다.
# 이를 통해 if문 순서(queue에 삽입되는 순서)는 +1 보다 -1을 먼저 진행해야한다. (*2는 우선순위가 있기에 상관없다.)

def bfs():
    queue = deque()
    queue.append(N)
    dist[N] = 0 # 초기값 설정 시작이 모두 -1이므로

    while queue:
        x = queue.popleft()

        if x == K:
            print(dist[K])
            break

        if 0 <= 2*x < MAX and dist[2*x] == -1 :
            # dist[x] 가 0에서 0일 경우 조건 파악을 못함
            #이동은 했으나 이동을 한 것을 알 수 없음
            dist[2*x] = dist[x] # 이동 횟수(시간) 0초 이므로 이전값으 그래도 이동
            queue.appendleft(2*x)

        if 0 <= x-1 < MAX and dist[x-1] == -1:
            dist[x-1] = dist[x] + 1 # 이동 횟수 1초
            queue.append(x-1)

        if 0 <= x+1 < MAX and dist[x+1] == -1:
            dist[x+1] = dist[x] + 1 # 이동횟수 1초
            queue.append(x+1)


bfs()

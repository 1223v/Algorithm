from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)
move = [0] * (MAX+1)



def path(x):
    result = []
    tmp = x
    for _ in range(dist[x]+1):
        result.append(tmp)
        tmp = move[tmp] # x -> x의 이전값(move[x]) -> x의 이전의 이전값(move[move[x]])

    print(' '.join(map(str, result[::-1]))) # 역순으로 출력

def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()

        # 종료조건
        if x == K:
            print(dist[x]) # K값의 이동한 횟수
            path(x) # 경로 추적



        for i in (x-1, x+1, 2*x):
            if 0<= i <= MAX and not dist[i]:
                dist[i] = dist[x] + 1 # 횟수 추가
                queue.append(i)
                move[i] = x # 이전값을 현재값에 저장 | i+1 -> i -> x


bfs()
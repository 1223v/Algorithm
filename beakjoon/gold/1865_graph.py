import sys
input = sys.stdin.readline


TC = int(input())

def bf():

    for i in range(N):
        for j in range(len(edges)):
            start, end, time_value = edges[j]
            if dist[end] > dist[start] + time_value:
                dist[end] = dist[start] + time_value
                if i == N-1:
                    return True

    return False

for _ in range(TC):
    N, M, W = map(int,input().split()) # 지점, 도로 갯수, 웜홀 갯수
    edges = []
    dist = [sys.maxsize] * (N+1)

    for _ in range(M): # 양방향
        S, E, T = map(int,input().split()) # 시작점, 끝점, 걸리는 시간
        edges.append((S,E,T))
        edges.append((E, S, T))


    for _ in range(W): # 한방향
        S, E, T = map(int, input().split())  # 시작점, 끝점, 줄어드는 시간
        edges.append((S, E, -T))



    if bf():
        print("YES")
    else:
        print("NO")
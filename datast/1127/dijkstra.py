def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])  # 거리 배열 초기화
    dist[start] = 0  # 시작 정점까지의 거리는 0
    path = [start] * vsize  # 경로 배열 초기화
    found = [False] * vsize  # 방문 여부 배열 초기화
    found[start] = True  # 시작 정점은 이미 방문한 상태

    for i in range(vsize - 1):  # 모든 정점을 처리할 때까지 반복
        print("Step%2d: " % (i + 1), dist)
        u = getMinVertex(dist, found)  # 현재 방문하지 않은 정점 중 최소 거리 정점 선택
        if u == -1:  # 선택할 정점이 없으면 중단
            break

        found[u] = True  # 선택한 정점을 방문 처리

        for w in range(vsize):  # 선택한 정점의 인접 정점 확인
            if not found[w] and adj[u][w] != INF:  # 방문하지 않은 정점 중에서
                if dist[u] + adj[u][w] < dist[w]:  # 더 짧은 경로가 있다면
                    dist[w] = dist[u] + adj[u][w]  # 거리 갱신
                    path[w] = u  # 경로 갱신

    return path

def getMinVertex(dist, selected):
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:  # 방문하지 않은 정점 중 최소 거리 정점 찾기
            mindist = dist[v]
            minv = v
    return minv

# 상수 정의
INF = 9999

# 정점 및 가중치 행렬 정의
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [0, 7, INF, INF, 3, 10, INF],
    [7, 0, 4, 10, 2, 6, INF],
    [INF, 4, 0, 2, INF, INF, INF],
    [INF, 10, 2, 0, 11, 9, 4],
    [3, 2, INF, 11, 0, 13, 5],
    [10, 6, INF, 9, 13, 0, INF],
    [INF, INF, INF, 4, 5, INF, 0]
]

# 실행
print("Shortest Path By Dijkstra Algorithm")
start = 0  # 시작 정점은 0번(A)
path = shortest_path_dijkstra(vertex, weight, start)

# 결과 출력
def print_paths(vtx, path, start):
    for i in range(len(vtx)):
        if i != start:
            print(f"Shortest path to {vtx[i]}: ", end="")
            trace_path(i, path, vtx)
            print()

def trace_path(v, path, vtx):
    if path[v] == v:
        print(vtx[v], end="")
    else:
        trace_path(path[v], path, vtx)
        print(f" -> {vtx[v]}", end="")

print_paths(vertex, path, start)

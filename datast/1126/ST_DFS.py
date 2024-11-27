# DFS 기반 간선 출력 함수
def ST_DFS(vtx, adj, s, visited):
    visited[s] = True  # 현재 정점 방문 처리
    for v in range(len(vtx)):  # 모든 정점을 탐색
        if adj[s][v] != 0:  # 정점이 연결되어 있으면
            if not visited[v]:  # 방문하지 않은 정점이면
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력
                ST_DFS(vtx, adj, v, visited)  # 재귀적으로 다음 정점 탐색

# 정점 리스트와 인접 행렬 정의
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adj = [
    [0, 1, 1, 0, 0, 0, 0, 0],  # A와 연결된 정점
    [1, 0, 0, 1, 0, 0, 0, 0],  # B와 연결된 정점
    [1, 0, 0, 0, 1, 0, 0, 0],  # C와 연결된 정점
    [0, 1, 0, 0, 1, 1, 0, 0],  # D와 연결된 정점
    [0, 0, 1, 1, 0, 0, 1, 0],  # E와 연결된 정점
    [0, 0, 0, 1, 0, 0, 0, 1],  # F와 연결된 정점
    [0, 0, 0, 0, 1, 0, 0, 0],  # G와 연결된 정점
    [0, 0, 0, 0, 0, 1, 0, 0]   # H와 연결된 정점
]

# DFS 탐색 수행
print('DFS 탐색 간선 출력 (출발: A): ', end="")
ST_DFS(vtx, adj, 0, [False] * len(vtx))  # 정점 A에서 시작
print()

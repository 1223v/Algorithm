# DFS 함수 정의
def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')  # 현재 정점을 출력
    visited[s] = True       # 현재 정점을 방문 처리

    # 모든 정점 확인
    for v in range(len(vtx)):
        if adj[s][v] != 0:  # 인접 행렬에서 연결 여부 확인
            if not visited[v]:  # 방문하지 않은 경우
                DFS(vtx, adj, v, visited)  # 재귀적으로 탐색

# 정점 리스트와 인접 행렬 정의
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edge = [
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
print('DFS(출발: A) : ', end="")
DFS(vtx, edge, 0, [False] * len(vtx))  # 정점 A에서 시작
print()

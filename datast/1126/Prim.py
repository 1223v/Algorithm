# 무한대를 나타내는 값
INF = 9999

# 최소 거리 정점을 선택하는 함수
def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

# Prim 알고리즘
def MSTPrim(vertex, adj):
    vsize = len(vertex)  # 정점의 개수
    dist = [INF] * vsize  # 최소 거리 초기화
    selected = [False] * vsize  # 정점 선택 여부
    dist[0] = 0  # 시작 정점의 거리 0 설정

    for i in range(vsize):  # 모든 정점 탐색
        u = getMinVertex(dist, selected)  # 최소 거리 정점 선택
        selected[u] = True  # 선택 완료
        print(vertex[u], end=' ')  # 선택된 정점 출력

        # 선택된 정점과 연결된 간선 업데이트
        for v in range(vsize):
            if adj[u][v] is not None:  # 간선이 존재하면
                if not selected[v] and adj[u][v] < dist[v]:  # 더 짧은 거리라면 업데이트
                    dist[v] = adj[u][v]
    print()  # 줄 바꿈

# 정점 리스트와 인접 행렬 정의
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [None, 29, None, None, None, 10, None],  # A
    [29, None, 16, None, None, None, 15],   # B
    [None, 16, None, 12, None, None, None], # C
    [None, None, 12, None, 22, None, 18],   # D
    [None, None, None, 22, None, 27, 25],   # E
    [10, None, None, None, 27, None, None], # F
    [None, 15, None, 18, 25, None, None]    # G
]

# Prim 알고리즘 실행
MSTPrim(vertex, weight)

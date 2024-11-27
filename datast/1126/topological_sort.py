def topological_sort_AM(vertex, edge):
    n = len(vertex)          # 정점의 개수
    inDeg = [0] * n          # 진입 차수를 저장할 리스트

    # 진입 차수 계산
    for i in range(n):
        for j in range(n):
            if edge[i][j] > 0:  # 간선이 존재하면
                inDeg[j] += 1   # 진입 차수 증가

    vlist = []               # 진입 차수가 0인 정점을 저장할 리스트
    for i in range(n):
        if inDeg[i] == 0:    # 진입 차수가 0인 정점 찾기
            vlist.append(i)

    # 위상 정렬 수행
    while len(vlist) > 0:
        v = vlist.pop()      # 리스트에서 정점 꺼내기
        print(vertex[v], end=' ')  # 정점 출력

        for u in range(n):
            if edge[v][u] > 0:  # 정점 v에서 u로 간선이 있으면
                inDeg[u] -= 1   # 진입 차수 감소
                if inDeg[u] == 0:  # 진입 차수가 0이 된 정점을 추가
                    vlist.append(u)

# 정점 리스트와 인접 행렬 정의
vertex = ['A', 'B', 'C', 'D', 'E', 'F']
graphAM = [
    [0, 0, 1, 1, 0, 0],  # A -> C, A -> D
    [0, 0, 0, 1, 1, 0],  # B -> D, B -> E
    [0, 0, 0, 1, 0, 1],  # C -> D, C -> F
    [0, 0, 0, 0, 0, 1],  # D -> F
    [0, 0, 0, 0, 0, 1],  # E -> F
    [0, 0, 0, 0, 0, 0]   # F (종료 노드)
]

# 위상 정렬 수행
print('topological_sort: ', end="")
topological_sort_AM(vertex, graphAM)
print()

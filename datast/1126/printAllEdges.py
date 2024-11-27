def printAllEdges(vlist, W):
    # 모든 간선을 출력
    for i in range(len(vlist)):         # 모든 정점 i에 대해
        for j in range(i + 1, len(vlist)):  # 정점 i 이후의 정점 j 탐색
            if W[i][j] is not None and W[i][j] != 0:  # 간선이 존재하면
                print("(%s, %s, %d)" % (vlist[i], vlist[j], W[i][j]), end=' ')
    print()  # 출력 완료 후 줄 바꿈

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

# 모든 간선 출력
printAllEdges(vertex, weight)

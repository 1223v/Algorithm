def weightSum(vlist, W):
    sum = 0  # 가중치의 합 초기화

    # 인접 행렬의 삼각 영역만 탐색
    for i in range(len(vlist)):         # 모든 정점 i에 대해
        for j in range(i + 1, len(vlist)):  # 정점 i 이후의 정점 j 탐색
            if W[i][j] is not None:         # 간선이 존재하면
                sum += W[i][j]             # 가중치를 합산

    return sum  # 전체 가중치 합 반환

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

# 가중치의 합 계산
print('AM : weight sum =', weightSum(vertex, weight))

def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = [list(row) for row in adj]  # 가중치 행렬 복사

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]  # 경로 갱신

    printA(A)

def printA(A):
    vsize = len(A)
    print("==========================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end="")
            else:
                print(f"%4d " % A[i][j], end="")
        print()

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
print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vertex, weight)
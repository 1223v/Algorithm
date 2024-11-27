from queue import Queue

# BFS 함수 정의
def BFS_AL(vtx, aList, s):
    n = len(vtx)               # 정점의 개수
    visited = [False] * n      # 방문 여부 초기화

    Q = Queue()                # 큐 생성
    Q.put(s)                   # 시작 정점을 큐에 삽입
    visited[s] = True          # 시작 정점을 방문 처리

    while not Q.empty():
        s = Q.get()            # 큐에서 정점 꺼내기
        print(vtx[s], end=' ') # 정점 출력

        # 인접 리스트를 통해 연결된 모든 정점 탐색
        for v in aList[s]:
            if not visited[v]:  # 방문하지 않은 정점인 경우
                Q.put(v)        # 큐에 삽입
                visited[v] = True  # 방문 처리

# 정점 리스트와 인접 리스트 정의
vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
aList = [
    [1, 2],    # A와 연결된 정점
    [0, 3],    # B와 연결된 정점
    [0, 4],    # C와 연결된 정점
    [1, 4, 5], # D와 연결된 정점
    [2, 3, 6], # E와 연결된 정점
    [3, 7],    # F와 연결된 정점
    [4],       # G와 연결된 정점
    [5]        # H와 연결된 정점
]

# BFS 탐색 수행
print('BFS_AL(출발: A): ', end="")
BFS_AL(vtx, aList, 0)  # 정점 A에서 시작
print()

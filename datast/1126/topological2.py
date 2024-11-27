from queue import Queue

def topological_sort_AM(vertex, edge):
    n = len(vertex)          # 정점의 개수
    inDeg = [0] * n          # 진입 차수를 저장할 리스트

    # 진입 차수 계산
    for i in range(n):
        for j in range(n):
            if edge[i][j] > 0:  # 간선이 존재하면
                inDeg[j] += 1   # 진입 차수 증가

    vlist = Queue()          # 진입 차수가 0인 정점을 저장할 큐
    for i in range(n):
        if inDeg[i] == 0:    # 진입 차수가 0인 정점 찾기
            vlist.put(i)

    # 위상 정렬 수행
    result = []
    while not vlist.empty():
        v = vlist.get()      # 큐에서 정점 꺼내기
        result.append(vertex[v])  # 정점 저장

        for u in range(n):
            if edge[v][u] > 0:  # 정점 v에서 u로 간선이 있으면
                inDeg[u] -= 1   # 진입 차수 감소
                if inDeg[u] == 0:  # 진입 차수가 0이 된 정점을 추가
                    vlist.put(u)

    return result


# 정점 리스트와 인접 행렬 정의
vertex = ['점화', '냄비에 물 붓기', '라면 넣기', '계란 풀기', '라면 봉지 뜯기', '스프 넣기']
graphAM = [
    [0, 1, 1, 1, 0, 0],  # 점화
    [0, 0, 0, 0, 1, 0],  # 냄비에 물 붓기
    [0, 0, 0, 0, 0, 1],  # 라면 넣기
    [0, 0, 0, 0, 0, 1],  # 계란 풀기
    [0, 0, 1, 0, 0, 0],  # 라면 봉지 뜯기
    [0, 0, 0, 0, 0, 0]   # 스프 넣기
]

# 위상 정렬 수행
print('위상 정렬 결과:', ' -> '.join(topological_sort_AM(vertex, graphAM)))

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):

    dx = [0, 0, -1, 1] # 상하좌우 좌표를 위한 dx, dy 리스트 선언
    dy = [1, -1, 0, 0]

    for i in range(4): # X,Y의 상하좌우의 좌표 nx, ny를 돌며, 배추가 있는지 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n): #nx, ny가 리스트 인덱스 범위를 초과하지 않는지 검증
            if field[ny][nx] == 1: # 그후, 배추 검증, 배추가 존재한다면
                field[ny][nx] = 0 # 방문표시하여 더이상 배추를 없는 취급함
                dfs(nx, ny) # 다시 dfs 호출 반복

for _ in range(int(input())):
    m, n, k = map(int,input().split()) # 배추 밭 가로, 세로, 배추 수 입력
    field = [[0 for _ in range(m)] for _ in range(n)] # 배추 크기 만큼 2차원 리스트 0으로 초기화
    count = 0 # 필요 벌레 수

    for _ in range(k): # 배추 수 만큼 돌면서 배추 좌표 입력 받고 리스트에 표시
        x,y = map(int, input().split())
        field[y][x] = 1

    for x in range(m): # 2차원 리스트를 돌면서 배추 검증
        for y in range(n):
            if field[y][x] == 1: # 배추라면 dfs 호출 벌레 한마리 카운트
                dfs(x,y) # 상하좌우가 연결되어 있다면, 한마리로 커버 가능하기에 연결된 애들은 묶음으로 표시
                count += 1
    print(count)
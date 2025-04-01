import sys
input = sys.stdin.readline

# 국경선을 공유하는 두 나라의 인구 차이가 L 명 이상 R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 염
# 위 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작함
# 국경선이 열려 있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루동안은 연합
# 연합을 이루고 있는 각 칸의 인구수는
#   연합의 인구수 / 연합을 이루고 있는 칸의 개수
# 연합을 해체하고 모든 국경선을 닫는다.



N, L,R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[[] for _ in range(N)] for _ in range(N)]

# 국경선을 공유하는 두 나라의 인구 차이가 L 명 이상 R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 염
def openCountry():

    for i in range(N):
        for j in range(N):
            if
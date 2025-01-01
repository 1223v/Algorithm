# N = 동물 수
# M = 총 쏘는 곳 갯수
# (aj, bj) = 동물 좌표
# L = 총 사정거리
# 사대 간의 거리 공식 abs(xi - aj) + bj
#
import sys
input = sys.stdin.readline

M, N, L = map(int,input().split())
gun_point = sorted(list(map(int,input().split())))
animal_point = [list(map(int,input().split())) for _ in range(N)]
animaled_point = [0] * N
result = 0

for i in range(len(animal_point)):

    start = 0
    end = len(gun_point)-1

    while start < end:
        mid = (start + end) // 2

        if gun_point[mid] < animal_point[i][0]:
            start = mid + 1

        else:
            end = mid

    if abs(gun_point[end] - animal_point[i][0]) + animal_point[i][1] <= L:
         animaled_point[i] = 1

    elif end+1 < len(gun_point)-1 and abs(gun_point[end+1] - animal_point[i][0]) + animal_point[i][1] <= L:
        animaled_point[i] = 1

    elif end > 0 and abs(gun_point[end-1] - animal_point[i][0]) + animal_point[i][1] <= L:
        animaled_point[i] = 1


print(animaled_point.count(1))


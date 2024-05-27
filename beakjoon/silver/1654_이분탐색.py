import sys

input = sys.stdin.readline

N,K = map(int, input().split()) #가지고 있는 랜선의 개수 N, 필요한 랜선의 개수 K
lis = [int(input()) for _ in range(N)] # 가지고 있는 랜선들의 길이

s = 1 # 최소 길이를 1로 설정
e = max(lis) # 가지고 있는 랜선들 중 가장 긴 길이로 설정

while s <= e: # 이분 탐색 시작. s > e가 될때까지 반복
    mid = (s+e)//2 # 중간 값 설정
    LAN = 0 # 나눈 랜선의 개수 초기화
    for i in lis: # 랜선을 mid의 개수로 잘랐을 때, 잘라진 랜선의 개수를 구하기
        LAN += i // mid
    if LAN >= K: # 랜선의 개수가 K개 이상 만들 수 있는 경우
        s = mid + 1 # mid + 1부터 e 까지 탐색  => 길이를 좀 늘리기
    else: # 필요한 랜선의 개수를 만들 수 없는 경우
        e = mid - 1 # s부터 mid -1까지 탐색 => 길이를 좀 줄이기

print(e) # s > e가 될때, e 값이 가장 긴 랜선의 길이

#정수 N, M을 입력 받기
n, m = map(int, input().split())

# N 개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

#한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행 보텀업
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1 ):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

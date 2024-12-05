T = int(input())

for test_case in range(1, T + 1):
    N, D, X = map(int,input().split()) # 결과 박수의 갯수, 공을 빼는 시작점, 끝나는 순서
    s = list(map(int,input().split()))
    tmp = [0] * N # 현황
    check = s[D-1] # 종료조건 값 : 현황의 값과 결과 박스의 값과 동일할 경우 종료
    cnt = 0 # 선택된 박스 공 갯수
    i = D # 시작점
    #result = cal(N, s ,D, X)
    while True:
        i = i % N
        tmp[i] += 1 # 현황값 증가
        cnt += 1 # 쓰는 공 갯수 증가
        i += 1 # 순회
        if tmp[D-1] == check and i == X: # 현황의 값과 결과 박스의 값과 동일할 경우 종료
            break
    print("#%d %d" % (test_case, cnt))
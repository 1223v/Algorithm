import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

S = [0] * N

for i in range(1,N):
    insert_point = i
    insert_value = A[i]

    for j in range(i-1,-1,-1): # for j 를 i-1 ~ 0까지 뒤에서 부터 반복
        if A[j] < A[i]: # 선택된 값보다 이후 배열이 작은 경우 해당 포인트 값에 +1 한값 저장
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0

    for j in range(i, insert_point, -1):
        A[j] = A[i-1]

    A[insert_point] = insert_value

S[0] = A[0]
for i in range(1,N): # 합배열 만들기
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0,N): # 합배열 총합 구하기
    sum += S[i]

print(sum)
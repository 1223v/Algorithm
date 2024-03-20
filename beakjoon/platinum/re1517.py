import sys

input = sys.stdin.readline
result = 0 #swap의 갯수

def merge_sort(s, e):
    global result
    if e-s < 1: return # 더이상 자를 수 없는 경우
    m = int(s+(e-s) / 2)
    merge_sort(s,m) #반 자른거
    merge_sort(m+1, e) # 나머지 반
    for i in range(s, e + 1): # A 데이터 복사
        tmp[i] = A[i]

    k=s
    index1 = s # 포인트
    index2 = m+1 # 2번째 포인트
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k # swap 값 카운트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1

    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1



N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
tmp = [0] * int(N+1)





merge_sort(1,N)
print(result)
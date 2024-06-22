import sys
input = sys.stdin.readline
result = 0

def merge_sort(s,e):
    global result
    if e-s < 1: return
    m = int(s+(e-s)/2)
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s,e+1):
        tmp[i] = A[i]
    k =s
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e:
        # 로직을 수행하면서 뒤쪽 데이터값이 더 작아 선택될 때, swap이 일어난 것과 동일한 것이기 때문에 현재 남은 앞쪽 그룹 데이터의
        # 개수 만금 결괏값에 더해줌
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k # 뒤쪽 데이터 값이 더 작으면 결괏값 업데이트 k에서 부터 index2까지 swap되는 것이므로 index-k
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m :
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1


N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
tmp = [0] * int(N+1)
merge_sort(1,N)
print(result)
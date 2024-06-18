import sys
input = sys.stdin.readline

A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max]:
            Max = j

    if A[i] < A[Max]: # 역순 정렬이므로
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp


print(''.join(A))
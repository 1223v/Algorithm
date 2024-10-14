import sys
input = sys.stdin.readline

A,B = input().rstrip().split()
result = []
for i in range(len(B)-len(A)+1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count += 1
    result.append(count)

print(min(result))
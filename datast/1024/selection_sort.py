def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i + 1)

def printStep(A, step):
    print(f"{step}: {A}")

# 예시 리스트
A = [64, 25, 12, 22, 11]
selection_sort(A)

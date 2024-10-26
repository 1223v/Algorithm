def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)

def printStep(A, step):
    print(f"{step}: {A}")

# 예시 리스트
A = [64, 25, 12, 22, 11]
insertion_sort(A)

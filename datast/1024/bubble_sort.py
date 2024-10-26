def bubble_sort(A):
    n = len(A)
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                bChanged = True
        if not bChanged:
            break
        printStep(A, n - i)

def printStep(A, step):
    print(f"{step}: {A}")


A = [64, 25, 12, 22, 11]
bubble_sort(A)

def sortGapInsertion(A, first, last, gap):
    for i in range(first + gap, last + 1, gap):
        key = A[i]
        j = i - gap
        while j >= first and key < A[j]:
            A[j + gap] = A[j]
            j = j - gap
        A[j + gap] = key


def shell_sort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        if (gap%2) == 0: gap += 1
        for i in range(gap):
            sortGapInsertion(A,i,n-1,gap)
        print('     Gap=',gap,A)
        gap = gap // 2
            
data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
shell_sort(data)
print("result : ", data)


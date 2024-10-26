def binary_search_iterative(A, key):
    low = 0
    high = len(A) - 1

    while low <= high:
        middle = (low + high) // 2

        if A[middle] == key:
            return middle
        elif A[middle] > key:
            high = middle - 1
        else:
            low = middle + 1

    return -1



A = [11, 22, 33, 44, 55, 66, 77, 88, 99]


key = 55


result = binary_search_iterative(A, key)

if result != -1:
    print(result)
else:
    print("없음")

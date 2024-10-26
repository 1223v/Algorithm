def binary_search_recursive(A, key, low, high):

    if low > high:
        return -1

    middle = (low + high) // 2

    if key == A[middle]:
        return middle

    elif key < A[middle]:
        return binary_search_recursive(A, key, low, middle - 1)

    else:
        return binary_search_recursive(A, key, middle + 1, high)



A = [11, 22, 33, 44, 55, 66, 77, 88, 99]


key = 55
low = 0
high = len(A) - 1


result = binary_search_recursive(A, key, low, high)

if result != -1:
    print(result)
else:
    print("없음")

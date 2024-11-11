def solution(arr):
    result = []

    for i in arr:
        if result:
            if result[-1] != i:
                result.append(i)
        else:
            result.append(i)
    return result
def bisect_left(a,x, lo=0, hi=None):
    """x를 정렬된 리스트 a에 삽입할 수 있는 가장 왼쪽 인덱스를 반환"""

    if lo < 0:
        raise ValueError('lo must be non-negative')

    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1

        else:
            hi = mid

    return lo

a = [1, 3, 4, 4, 4, 4, 7]

print(bisect_left(a, 4))    # 2
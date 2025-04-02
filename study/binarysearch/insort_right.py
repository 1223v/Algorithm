from bisect import bisect_right

def insort_right(a,x,lo=0, hi=None):
    """x를 a에 정렬을 유지하면서 가장 왼쪽에 삽입"""
    i = bisect_right(a,x)
    a.insert(i,x)

a = [1, 3, 4, 7]

insort_right(a, 2)
print(a)                    # [1, 2, 3, 4, 7]
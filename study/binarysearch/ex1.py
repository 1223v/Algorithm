import bisect

a = [1,3,4,7]

# bisect_left
idx = bisect.bisect_left(a,4)
print(idx) # 2

# bisect_right
idx = bisect.bisect_left(a,4)
print(idx) # 2

# insort_left
bisect.insort_left(a,2)
print(a) # [1, 2, 3, 4, 7]

# insort_right
bisect.insort_right(a,4)
print(a) # [1, 2, 3, 4, 4, 7]

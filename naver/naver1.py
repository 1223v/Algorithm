from collections import Counter
def sol(arr):
    count = Counter(arr)
    most_common_value, most_common_count = count.most_common(1)[0]
    return 0 if most_common_value == min(arr) else most_common_value


a = [3,1,4,1,5]
print(sol(a))

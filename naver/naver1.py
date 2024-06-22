from collections import Counter
def sol(arr):
    count = Counter(arr)
    most_common_value, most_common_count = count.most_common(1)[0]
    return 0 if most_common_value == min(arr) else most_common_value


a = [7,1,2,8,2]
print(sol(a))

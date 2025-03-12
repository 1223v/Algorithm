import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().rstrip()
    m = int(input())
    dict_s = defaultdict(list)

    for i in range(len(s)):
        if s.count(s[i]) >= m:
            dict_s[s[i]].append(i)

    if not dict_s:
        print(-1)

    else:
        max_value = 0
        min_value = float('inf')

        for a in dict_s:
            for i in range(len(dict_s[a]) - m + 1):
                length = dict_s[a][i+m-1] - dict_s[a][i] + 1

                max_value = max(max_value, length)
                min_value = min(min_value, length)
        print(min_value, max_value)
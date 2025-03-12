import sys
from collections import defaultdict
input = sys.stdin.readline


n = int(input())
for _ in range(n):
    clothes_count = int(input())
    cloth_dicts = defaultdict(list)

    for _ in range(clothes_count):
        cloth_name, cloth_tag = map(str, input().rstrip().split())
        cloth_dicts[cloth_tag].append(cloth_name)


    tmp = 1
    for i in cloth_dicts:

        tmp *= len(cloth_dicts[i])+1


    print(tmp-1)



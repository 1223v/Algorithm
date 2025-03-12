# https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin

tree = {}
num_count = 0
for i in input:
    if i == '\n':
        break
    x = i.rstrip()
    num_count += 1

    if x in tree:
        tree[x] += 1

    else:
        tree[x] = 1

tree_sort = sorted(tree.items())
for tree_name,num in tree_sort:
    k = (num / num_count) * 100
    print(tree_name,format(k,".4f"))



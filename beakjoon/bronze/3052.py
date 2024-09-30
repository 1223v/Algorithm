import sys
input = sys.stdin.readline

lst = []
for _ in range(10):
    x = int(input())
    lst.append(x % 42)

print(len(set(lst)))

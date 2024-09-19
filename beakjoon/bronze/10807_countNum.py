import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int,input().split()))
find_num = int(input())

print(s.count(find_num))
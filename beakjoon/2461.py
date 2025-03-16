import sys
input = sys.stdin.readline
from itertools import product

N,M = map(int,input().split())
graph = [sorted(list(map(int,input().split()))) for _ in range(N)]


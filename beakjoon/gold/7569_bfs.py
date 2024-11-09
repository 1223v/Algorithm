import sys
input = sys.stdin.readline

N, M, H = map(int,input().split())

s = [[list(map(int,input().split())) for _ in range(M)] for _ in range(H)]

di = []
dj = []
dz = []
import sys
input = sys.stdin.readline

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]
white = 0
blue = 0
def div(di,dj,n):
    global blue, white
    color = s[di][dj]
    for i in range(di,di+n):
        for j in range(dj,dj+n):
            if color != s[i][j]:
                m = n//2
                div(di,dj,m)
                div(di,dj+m,m)
                div(di+m,dj,m)
                div(di+m,dj+m,m)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

div(0,0,N)
print(white)
print(blue)
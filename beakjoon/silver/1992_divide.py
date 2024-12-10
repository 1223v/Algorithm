import sys
input = sys.stdin.readline

N = int(input())
s = [list(map(int,input().rstrip())) for _ in range(N)]


result = ""
def div(di,dj,n):
    global result
    color = s[di][dj]

    for i in range(di,di+n):
        for j in range(dj, dj+n):
            if color != s[i][j]:
                result += "("
                m = n//2
                div(di,dj,m)
                div(di,dj+m,m)
                div(di+m, dj, m)
                div(di+m, dj+m, m)
                result += ")"
                return

    if color == 1:
        result += "1"

    else:
        result += "0"

div(0,0,N)
print(result)
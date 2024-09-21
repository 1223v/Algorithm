import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def solve(ci,cj,dr):
    cnt = 0
    while True:
        s[ci][cj] =2
        cnt += 1

        flag = 1
        while flag == 1:
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
                ni,nj = ci+di[nd], cj+dj[nd]
                if s[ni][nj] == 0:
                    ci,cj,dr = ni,nj,nd
                    flag = 0
                    break
            else:
                bi,bj = ci-di[dr], cj-dj[dr]
                if s[bi][bj] == 1:
                    return cnt
                else:
                    ci,cj = bi,bj

n,m = map(int, input().split())
si,sj,dr = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(n)]

answer = solve(si, sj, dr)
print(answer)
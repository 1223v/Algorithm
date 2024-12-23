import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
s = [ input().rstrip() for _ in range(N)]
di = [1,-1, 0, 0]
dj = [0,0,1,-1]

B = []
R = []
O = []

for i in range(N):
    for j in range(M):
        if s[i][j] == 'B':
            B.append((i,j))

        elif s[i][j] == 'R':
            R.append((i,j))

        elif s[i][j] == 'O':
            O.append((i,j))

queue = deque()
queue.append((R[0][0], R[0][1], B[0][0], B[0][1],0))

visited = []
visited.append((R[0][0], R[0][1], B[0][0], B[0][1]))

def bfs():


    while queue:

        Rci,Rcj,Bci,Bcj,count= queue.popleft()

        if count > 10:
            return -1

        if s[Rci][Rcj] == 'O':
            return count


        for i in range(4):
            Rni,Rnj,Bni,Bnj = Rci,Rcj,Bci,Bcj

            while True:
                Rni += di[i]
                Rnj += dj[i]

                if s[Rni][Rnj] == '#':
                    Rni -= di[i]
                    Rnj -= dj[i]
                    break

                if s[Rni][Rnj] == 'O':
                    break

            while True:
                Bni += di[i]
                Bnj += dj[i]

                if s[Bni][Bnj] == '#':
                    Bni -= di[i]
                    Bnj -= dj[i]
                    break

                if s[Bni][Bnj] == 'O':
                    break

            if s[Bni][Bnj] == 'O':
                continue

            if Rni == Bni and Rnj == Bnj:
                if abs(Rni - Rci) + abs(Rnj - Rcj) > abs(Bni - Bci) + abs(Bnj - Bcj):
                    Rni -= di[i]
                    Rnj -= dj[i]
                else:
                    Bni -= di[i]
                    Bnj -= dj[i]

            if (Rni,Rnj,Bni,Bnj) not in visited:
                queue.append((Rni,Rnj,Bni,Bnj,count+1))
                visited.append((Rni,Rnj,Bni,Bnj))


    return -1


print(bfs())


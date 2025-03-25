import sys
input = sys.stdin.readline

di,dj = [0,-1,0,1],[1,0,-1,0]
N = int(input())

graph = [[0] * 101 for _ in range(101)]


def drawing_dragons(y,x,d,g):

    lst = [(x,y)]
    lst.append((x+di[d],y+dj[d]))

    for _ in range(g):
        ci,cj = lst[-1]
        for i in range(len(lst)-2,-1,-1):
            ni,nj = lst[i]
            lst.append((ci-(cj-nj), cj+(ci-ni)))

    for i,j in lst:
        graph[i][j] = 1


def counting_dragons(graph):
    tmp = 0


    for i in range(100):
        for j in range(100):

            if graph[i][j] == graph[i+1][j] == graph[i+1][j+1] == graph[i][j+1] == 1:
                tmp += 1

    return tmp

for i in range(N):
    x,y,d,g = map(int,input().split())
    drawing_dragons(x,y,d,g)

result = counting_dragons(graph)
print(result)


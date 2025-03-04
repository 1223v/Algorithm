import sys
input = sys.stdin.readline

N,M,R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
R_lst = list(map(int,input().split()))



def sol1(tmp):
    global graph

    tmp2 = []
    for i in range(len(graph)-1,-1,-1):
        tmp2.append(tmp[i])

    graph = tmp2[::]

def sol2(tmp):
    global graph

    tmp2 = []
    for i in range(len(graph)):
        tmp2.append(tmp[i][::-1])

    graph = tmp2[::]



def sol3(tmp):
    global graph

    tmp3 = []
    for j in range(len(graph[0])):
        tmp2 = []
        for i in range(len(graph)-1,-1, -1):
            tmp2.append(tmp[i][j])


        tmp3.append(tmp2)


    graph = tmp3[::]



def sol4(tmp):
    global graph

    tmp3 = []
    for j in range(len(graph[0])-1, -1, -1):
        tmp2 = []
        for i in range(len(graph)):
            tmp2.append(tmp[i][j])

        tmp3.append(tmp2)
    graph = tmp3[::]

def sol5(tmp):
    global graph

    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []

    for i in range(len(graph)//2):
        dump = []
        for j in range(len(graph[0])//2):
            dump.append(tmp[i][j])
        tmp1.append(dump)

    for i in range(len(graph)//2):
        dump = []
        for j in range(len(graph[0])//2,len(graph[0])):
            dump.append(tmp[i][j])
        tmp2.append(dump)

    for i in range(len(graph)//2,len(graph)):
        dump = []
        for j in range(len(graph[0])//2):
            dump.append(tmp[i][j])
        tmp4.append(dump)


    for i in range(len(graph)//2,len(graph)):
        dump = []
        for j in range(len(graph[0])//2,len(graph[0])):
            dump.append(tmp[i][j])
        tmp3.append(dump)



    result = []
    for i in range(len(graph)):
        dump = []
        if i < len(graph)//2:
            dump += tmp4[i] + tmp1[i]

        else:

            dump += tmp3[i%(len(graph)//2)] + tmp2[i%(len(graph)//2)]

        result.append(dump)



    graph = result[::]


def sol6(tmp):
    global graph

    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []

    for i in range(len(graph) // 2):
        dump = []
        for j in range(len(graph[0]) // 2):
            dump.append(tmp[i][j])
        tmp1.append(dump)

    for i in range(len(graph) // 2):
        dump = []
        for j in range(len(graph[0]) // 2, len(graph[0])):
            dump.append(tmp[i][j])
        tmp2.append(dump)

    for i in range(len(graph) // 2, len(graph)):
        dump = []
        for j in range(len(graph[0]) // 2):
            dump.append(tmp[i][j])
        tmp4.append(dump)

    for i in range(len(graph) // 2, len(graph)):
        dump = []
        for j in range(len(graph[0]) // 2, len(graph[0])):
            dump.append(tmp[i][j])
        tmp3.append(dump)

    result = []
    for i in range(len(graph)):
        dump = []
        if i < len(graph) // 2:
            dump += tmp2[i] + tmp3[i]

        else:
            dump += tmp1[i%(len(graph)//2)] + tmp4[i%(len(graph)//2)]

        result.append(dump)

    graph = result[::]


for i in R_lst:

    if i == 1:
        sol1(graph)

    elif i == 2:
        sol2(graph)

    elif i == 3:
        sol3(graph)

    elif i == 4:
        sol4(graph)

    elif i == 5:
        sol5(graph)

    elif i == 6:
        sol6(graph)

for i in range(len(graph)):
     print(' '.join(map(str,graph[i])))

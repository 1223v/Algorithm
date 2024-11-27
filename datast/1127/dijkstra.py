def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    dist[start] = 0
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True

    for i in range(vsize):
        print("Step%2d: "%(i+1),dist)
        u = getMinVertex(dist, found)

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path

def choose_vertex(dist,found):
    min = INF
    minpos = -1


def getMinVertex(dist,selected):
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

INF = 9999   #복붙하세요!
vertex =   [  'A', 'B', 'C', 'D', 'E', 'F', 'G' ]
weight = [ [    0,   7, INF, INF,   3,  10, INF ],
           [    7,   0,   4,  10,   2,   6, INF ],
           [  INF,   4,   0,   2, INF, INF, INF ],
           [  INF,  10,   2,   0,  11,   9,   4 ],
           [    3,   2, INF,  11,   0,  13,   5 ],
           [   10,   6, INF,   9,  13,   0, INF ],
           [  INF, INF, INF,   4,   5, INF,   0 ]]
print("Shortest Path By Dijkstra Algorithm")
start = 0	# 시작 정점은 0번(A)
path = shortest_path_dijkstra(vertex, weight, start)

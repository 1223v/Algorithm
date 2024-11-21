cnt = 0


def solution(n, wires):
    global cnt
    s = [[] for _ in range(n + 1)]
    min_value = int(1e9)
    visited = [False] * (n + 1)
    result = []

    def dfs(v):
        global cnt
        cnt += 1
        visited[v] = True
        for i in s[v]:
            if not visited[i]:
                dfs(i)

    for k in range(len(wires)):
        result = []
        visited = [False] * (n + 1)
        for i in range(len(wires)):
            if k != i:
                s[wires[i][0]].append(wires[i][1])
                s[wires[i][1]].append(wires[i][0])

        for i in range(n):
            if not visited[i]:
                cnt = 0
                dfs(i)
                result.append(cnt)

        min_value = min(min_value,abs(result[1] - result[0]))

    return min_value
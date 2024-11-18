max_value = 0
def solution(k, dungeons):
    length = len(dungeons)

    visited = [False] * (length)

    def dfs(n, now, cnt):
        global max_value
        max_value = max(max_value, cnt)
        if length == n:
            return

        for i in range(length):
            if not visited[i] and dungeons[i][0] <= now:
                visited[i] = True
                dfs(n + 1, now - dungeons[i][1], cnt + 1)
                visited[i] = False

    dfs(0, k, 0)
    return max_value
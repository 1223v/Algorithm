

def dfs(v):
    global chk, visited
    if len(chk) == 6:
        print(' '.join(map(str,chk)))
        return

    for i in range(v,len(s)):
        if not visited[i]:
            visited[i] = True
            chk.append(s[i])
            dfs(i)
            visited[i] = False
            chk.pop()




while True:
    s = list(map(int, input().split()))

    if s[0] == 0:
        break
    visited = [False] * (len(s))
    chk = []
    dfs(1)
    #print()


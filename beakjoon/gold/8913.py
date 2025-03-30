import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    S = input().rstrip()

    chk = False
    visited = set()
    def dfs(s):
        global chk
        if chk:
            return

        if s in visited:
            return
        visited.add(s)

        if len(s) == 0:
            chk = True
            return

        if len(s) == 1:
            return

        for i in range(len(s)):

            if chk:
                return

            cnt = i
            for k in range(i,len(s)):

                if s[i] != s[k]:
                    break
                cnt = k


            if len(s) == cnt-i+1:
                dfs("")

            elif cnt-i+1 >= 2:

                dfs(s[:i] + s[cnt+1:])

    dfs(S)
    if chk:
        print(1)

    else:
        print(0)



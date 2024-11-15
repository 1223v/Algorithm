
TC = int(input())

def dfs(n,total):
    global min_value
    if N == n:
        if total >= H:
            min_value = min(total - H, min_value)
        return

    dfs(n+1, total+s[n])
    dfs(n+1, total)


for i in range(1,TC+1):
    N, H = map(int,input().split())
    min_value = int(1e9)
    s = list(map(int,input().split()))

    dfs(0,0)

    print(f"#{i} {min_value}")


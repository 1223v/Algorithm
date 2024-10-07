import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
cal_lst = list(map(int,input().split()))
min_value = 1e9
max_value = -1e9
def dfs(n, sm, plus, minus, mul, div):
    global max_value, min_value
    if N == n:
        max_value = max(max_value,sm)
        min_value = min(min_value,sm)
        return


    if plus != 0:
        dfs(n+1, sm+num[n], plus-1 , minus, mul, div)
    if minus != 0:
        dfs(n + 1, sm - num[n], plus, minus-1, mul, div)
    if mul != 0:
        dfs(n + 1, sm * num[n], plus, minus, mul-1, div)
    if div != 0:
        dfs(n + 1, int(sm / num[n]), plus, minus, mul, div-1)

dfs(1,num[0],cal_lst[0],cal_lst[1],cal_lst[2],cal_lst[3])

# 최대 값
print(max_value)

# 최소 값
print(min_value)
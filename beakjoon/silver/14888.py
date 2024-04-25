import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
add_num, minus_num, mul_num,div_num = map(int, input().split())


maximum = -1e9
minimum = 1e9

def dfs(depth,total,add_num, minus_num, mul_num,div_num):
    global maximum, minimum

    # 종료 조건 수식의 끝에 왔을 경우
    if depth == n:
        minimum = min(total, minimum)
        maximum = max(total,maximum)
        return

    # 독립적 분기 처리(elif 사용 x)
    if add_num:
        dfs(depth+1, total+nums[depth], add_num-1, minus_num, mul_num, div_num )

    if minus_num:
        dfs(depth+1, total-nums[depth], add_num, minus_num-1, mul_num, div_num)

    if mul_num:
        dfs(depth+1, total*nums[depth], add_num,minus_num, mul_num-1, div_num)

    if div_num:
        dfs(depth+1, int(total/nums[depth]), add_num, minus_num, mul_num, div_num-1)



dfs(1, nums[0], add_num, minus_num, mul_num,div_num)
print(maximum)
print(minimum)


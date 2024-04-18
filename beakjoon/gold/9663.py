import sys
input = sys.stdin.readline

n = int(input())

def check(start):
    for i in range(start):
        # 같은 행에 퀸이 있거나 대각선에 퀸이 있는경우
        if row[start] == row[i] or abs(row[start] - row[i]) == abs(start - i):
            return True

    return False



def dfs(start):

    global result

    if start == n:
        result += 1
        return


    for i in range(n):
        row[start] = i
        if not check(start):
            dfs(start + 1)


row = [0] * (n)
result = 0
dfs(0)

print(result)

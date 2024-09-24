import sys
input = sys.stdin.readline

n = int(input())
nums = ["1","2","3","4","5","6","7","8","9","0"]

def cal(s):
    s=s.replace(" ","")
    cnt = ""
    total =0
    for i in range(len(s)):
        if s[i] in nums:
            cnt += s[i]
        else:
            if cnt != "" and cnt != "-":
                total += int(cnt)
                if s[i] == "-":
                    cnt = "-"
                else:
                    cnt = ""

    if cnt != "" and cnt != "-":
        total += int(cnt)

    return total



def dfs(x, k, s): # x = 제한 값, k = 현재 값, s = 문자열
    # 탈출 조건
    if x == k:
        if cal(s) == 0:
            print(s)
        return



    # 공백인 경우
    dfs(x, k + 1, s + " " + str(k + 1))

    # + 인 경우
    dfs(x, k + 1, s + "+" + str(k + 1))

    # - 인 경우
    dfs(x, k + 1, s + "-"+str(k+1))





for _ in range(n):
    x = int(input())
    visited = [False] * (x+1)
    dfs(x,1,"1")
    print()
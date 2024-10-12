import sys
input = sys.stdin.readline

N = int(input())
s = list(map(str, input().split()))
visited = [False] * 10

max_value = 0
min_value = sys.maxsize
max_value_string = ""
min_value_string = ""

def check(current_string):

    global max_value_string, min_value_string,max_value, min_value

    if max_value < int(current_string):
        max_value = int(current_string)
        max_value_string = current_string


    if min_value > int(current_string):
        min_value = int(current_string)
        min_value_string = current_string


def dfs(n, current_value,current_string):

    if len(current_string) == N+1:

        check(current_string)
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            if current_value > -1:
                if s[n] == '<' and current_value < i:
                    dfs(n+1, i, current_string + str(i))
                elif s[n] == '>' and current_value > i:
                    dfs(n+1,i, current_string+str(i))
            else:
                dfs(n, i, current_string + str(i))

            visited[i] = False



dfs(0,-1,"")
print(max_value_string)
print(min_value_string)
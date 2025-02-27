import sys
input = sys.stdin.readline

s = list(map(str,input().rstrip()))

sort_s = sorted(list(map(str,s)))
visited = [0] * len(s)

while True:

    result = ""
    for i in range(len(s)):
        if visited[i] == 1:
            result += s[i]

    if len(result)>0:
        print(result)

    if len(result) == len(s):
        break

    tmp = []

    for i in range(len(s)):
        if visited[i] == 0:
            visited[i] = 1
            tmp_s = ""
            for j in range(len(s)):
                if visited[j] == 1:
                    tmp_s += s[j]
            tmp.append((tmp_s, i))
            visited[i] = 0



    if len(tmp) > 0:

        k = min(tmp)
        visited[k[1]] = 1





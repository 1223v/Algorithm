def solution(begin, target, words):
    answer = float('inf')

    visited = {}
    for i in words:
        if target == i:
            visited[i] = 1
        else:
            visited[i] = 0

    def check(s):
        cnt1 = 0
        for jz in range(len(s)):
            if s[jz] != begin[jz]:
                cnt1 += 1
        if cnt1 == 1:
            return True
        else:
            return False

    def dfs(n,ts,visited):
        nonlocal answer
        if ts not in words:
            answer = 0
            return

        elif check(ts):
            answer = min(n+1,answer)
            # print("정답",visited)
            return


        else:
            if n == len(words):
                return


            for i in words:
                if visited[i] == 0:
                    cnt = 0
                    for j in range(len(ts)):
                        if ts[j] != i[j]:
                            cnt += 1
                    if cnt == 1:

                        visited[i] = 1

                        dfs(n+1, i, visited)
                        visited[i] = 0



    dfs(0,target,visited)
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
def solution(tickets):
    answer = []
    visited = [0] * (len(tickets))

    def dfs(n, v, s):

        if n == len(tickets):
            s += "," + tickets[v][1]
            tmp = list(map(str, s.split(",")))
            answer.append(tmp)
            return


        for i in range(len(tickets)):
            if visited[i] == 0 and tickets[v][1] == tickets[i][0]:
                visited[i] = 1
                dfs(n + 1, i, s + "," + tickets[v][1])
                visited[i] = 0

    tickets.sort(key=lambda x: (x[1]))

    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visited[i] = 1
            dfs(1, i, "ICN")
            visited[i] = 0


    if len(answer) == 1:
        return answer[0]

    answer.sort()
    return answer[0]


print(solution([["ICN", "BBB"], ["BBB", "ICN"], ["ICN", "AAA"]]))
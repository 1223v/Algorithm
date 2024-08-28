import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
result = [0] * (n)
ans = []
for i in range(n):
    for j in range(n):
        if i != j:
            for x in range(5):
                if A[i][x] == A[j][x]:
                    result[i] += 1
                    break # 반례 주의! 가장 많은 학생과 같은 반이 된것이지 한사람과 많이 같은 반이 된 경우는 샐 필요 없음

if result.count(max(result)) > 1:
    for i in range(n):
        if result[i] == max(result):
            ans.append(i)

    print(min(ans) + 1)




else:
    print(result.index(max(result))+1)



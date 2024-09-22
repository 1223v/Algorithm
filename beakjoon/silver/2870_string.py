import sys
input = sys.stdin.readline

num = ["1","2","3","4","5","6","7","8","9","0"]
result = []
n = int(input())
for i in range(n):

    s = list(map(str, input().rstrip()))
    cnt = ""
    tmp = []
    for i in s:

        if i in num:
            cnt += i

        else:
            if cnt != "":
                tmp.append(int(cnt))
            cnt = ""

    if cnt != "":
        tmp.append(int(cnt))

    result += tmp

result.sort()

for i in result:
    print(i)


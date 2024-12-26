import sys
input = sys.stdin.readline

s = input().rstrip()
sort_s = sorted(list(set(s)))
tmp = []
count = dict()

for i in sort_s:
    count[i] = s.count(i)
    if count[i] %2:
        tmp.append(i)

if len(tmp)>1:
    print("I'm Sorry Hansoo")

else:
    result = ''
    for i in sort_s:
        result += i * (count[i]//2)

    if tmp:
        result += tmp[0] + result[::-1]
    else:
        result += result[::-1]

    print(result)
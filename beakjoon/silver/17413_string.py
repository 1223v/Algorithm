import sys
input = sys.stdin.readline

s = input().rstrip()
k = []
cnt = ""
for i in range(len(s)):
    if " " == s[i]:
        if "<" in cnt or ">" in cnt:
            cnt += " "
        else:
            k.append(cnt)
            k.append(" ")
            cnt= ""
        continue

    if "<" == s[i] and cnt != "":
        k.append(cnt)
        cnt =""


    cnt += s[i]
    if ">" == s[i]:
        k.append(cnt)
        cnt = ""
if cnt != "":
    k.append(cnt)


for i in k:
    if i.count("<") or i.count(">"):
        print(i, end="")
    else:
        print(i[::-1], end="")







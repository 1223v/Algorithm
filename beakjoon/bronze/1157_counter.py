A = input().upper()
setA = list(set(A))
cnt = []

for i in setA:
    cnt.append(A.count(i))


if cnt.count(max(cnt)) > 1:
    print("?")

else:

    print(setA[cnt.index(max(cnt))])


n = int(input())


for i in range(n):
    k = int(input())
    s = list(input().rstrip() for _ in range(k))
    checksum = False
    for x in range(k):
        for y in range(k):
            if x != y:
                tmp=s[x] + s[y]
                if tmp == tmp[::-1]:
                    print(tmp)
                    checksum = True
                    break
        if checksum:
            break
    if checksum == False:
        print(0)


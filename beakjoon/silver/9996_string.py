n = int(input())
origin_s1, origin_s2 = map(str,input().split('*'))

for _ in range(n):
    s = input()
    checksum = False
    if s[0:len(origin_s1)] == origin_s1:
        s=s.replace(origin_s1,"")
        checksum = True

    if checksum and s[len(s)-len(origin_s2):] == origin_s2:
        print("DA")
    else:
        print("NE")

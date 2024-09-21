import sys
input = sys.stdin.readline

while True:

    s = input().rstrip()
    if s == '#':
        break

    s = s[::-1]
    result = 0
    for i in range(len(s)):

        if '-' == s[i]:
            word = 0
        elif '\\' == s[i]:
            word = 1
        elif '(' == s[i]:
            word = 2
        elif '@' == s[i]:
            word = 3
        elif '?' == s[i]:
            word = 4
        elif '>' == s[i]:
            word = 5
        elif '&' == s[i]:
            word = 6
        elif '%' == s[i]:
            word = 7
        elif '/' == s[i]:
            word = -1



        result += word * (8**i)
    print(result)

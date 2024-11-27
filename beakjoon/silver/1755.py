import sys
input = sys.stdin.readline

x,y = map(int,input().split())

s = []
num_dic = {
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

for i in range(x,y+1):
    tmp = str(i)
    tmp_str1 = num_dic[tmp[0]]
    if len(tmp) > 1:
        tmp_str2 = num_dic[tmp[1]]
        s.append((tmp_str1+" "+tmp_str2,i))
    else:
        s.append((tmp_str1, i))
s.sort(key=lambda x: x[0])

for i in range(len(s)):
    if i % 10 == 0 and i != 0:
        print()
    print(s[i][1], end=' ')




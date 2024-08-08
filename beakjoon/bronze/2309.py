import sys
input = sys.stdin.readline

s = []
for i in range(9):
    n = int(input())
    s.append(n)


sum_num=sum(s)
chk = False

for i in range(9):
    for j in range(i+1,9):
        if s[i] + s[j] == sum_num - 100:

            del s[i] # 연속으로 쓸경우 인덱스가 밀리므로
            del s[j-1] # 여기서 -1을 해줘야 함

            chk=True
            break
    if chk:
        break



s.sort()
print('\n'.join(map(str, s)))

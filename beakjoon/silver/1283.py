# 먼저 하나의 옵션에 대해  살펴본다.
# 만약 왼쪽에서부터 오른쪽 순서로 단어의 첫 글자가 단축키로 아직 지정이 안 되어있다면
#       그 알파벳을 단축키로 지정

# 만약 모든 단어의 첫 글자가 이미 지정이 되어있다면,
#   왼쪽에서부터 차례대로 알파벳을 보면서 단축키로 지정 안 된 것이 있다면 단축키로 지정

# 어떠한 것도 단축키로 지정할 수 없다면 그냥 놔두며 대소문자를 구분치 않는다.

# 위의 규칙을 첫 번째 옵션부터 N번째 옵션까지 차례대로 적용한다.

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

commands = [input().rstrip() for _ in range(N)]

first_cache = {}
cache ={}

for s in commands:
    s_lst = list(map(str,s.split()))
    chk = False

    k = ""
    k1 = 0
    for i in s_lst:

        tmp = i.upper()
        if tmp[0] not in first_cache:
            first_cache[tmp[0]] = 1
            if len(tmp) > 1:
                k += "["+i[0]+"]"+i[1:]
            else:
                k += "[" + i[0] + "]"
            chk = True
            break
        k += i
        k += " "
        k1 += 1


    if len(s_lst)-1 > k1:
        for qi in range(k1+1,len(s_lst)):

            k += " "+s_lst[qi]
        k = k.rstrip()




    if chk:
        print(k)
        continue

    chk2 = False
    q = ""
    k2 = 0
    for j in s_lst:
        if len(j) > 1:
            for i in range(1,len(j)):
                tmp = j[i].upper()
                if tmp not in first_cache:
                    first_cache[tmp] = 1


                    if i < len(j)-1:
                        q += j[:i]+"["+j[i]+"]"+j[i+1:]
                    elif i == len(j) - 1:
                        q += j[:i]+ "[" + j[i] + "]"

                    chk2 = True
                    break

        if chk2:
            break

        q += j
        q += " "

        k2 += 1

    if len(s_lst)-1 > k2:
        for qi in range(k2+1,len(s_lst)):
            q += " " + s_lst[qi]

        q = q.rstrip()


    print(q)





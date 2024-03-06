from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
sorting_block = list(sys.stdin.readline().split())

visitS = set("".join(sorting_block))
d = deque([["".join(sorting_block), 0]])
solve = -1

while(d):
    word, cnt = d.popleft()
    tmpL = list(word)

    if tmpL == sorted(tmpL):
        solve = cnt
        break

    for i in range(n-m+1):
        newL = list(tmpL)# 복사본을 위한 list() 재선언
        revL = newL[i:i+m]
        revL.reverse()
        for j in range(m):
            newL[i+j] = revL[j]
        newWord = "".join(newL)
        if newWord not in visitS:
            visitS.add(newWord)
            d.append([newWord, cnt+1])


print(solve)

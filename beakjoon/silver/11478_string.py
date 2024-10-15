import sys
input = sys.stdin.readline

s = input().rstrip()

result_lst = []
for i in range(len(s)):
    for j in range(len(s)):
        if j + i + 1 <= len(s):
            tmp = s[j:j+i+1]
            result_lst.append(tmp)
        else:
            break

result_set = set(result_lst)
print(len(result_set))
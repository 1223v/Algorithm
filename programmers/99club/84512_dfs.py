cnt = 0
result = 0
text = ""
s_dict = {}
def dfs(n, s):
    global cnt, result, text

    if s == text:
        result = cnt
        return

    if len(s) == 5:
        return

    elif result == 0:
        for i in ["A", "E", "I", "O", "U"]:

            if s+i not in s_dict:

                s_dict[s+i] = 1
                cnt += 1
                dfs(n + 1, s + i)

def solution(word):
    global text
    text = word

    dfs(0,"")
    return result

print(solution("AAAAE"))
def solution(s):
    answer = []

    dic = {}
    k = [-1] * (len(s))
    for i in range(len(s)):
        if s[i] in dic:
            k[i]=i-dic[s[i]]
            dic[s[i]] = i

        else:
            dic[s[i]] = i

    return k

print(solution("banana"))
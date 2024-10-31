def solution(s):
    answer = 0
    x_count = 0
    x_notcount = 0
    x = ""

    for i in range(len(s)):

        if x == "":
            x = s[i]
            x_count = 1
            continue


        if x != s[i]:
            x_notcount +=1

        elif x == s[i]:
            x_count += 1

        if x_count == x_notcount:
            answer += 1
            x_count = 0
            x_notcount = 0
            x = ""


    if x != "":
        answer += 1

    return answer


print(solution("aaabbaccccabba"))
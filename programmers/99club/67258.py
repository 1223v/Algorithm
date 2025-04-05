from collections import defaultdict

def solution(gems):

    gems_length = len(gems)
    gems_set = set(gems)
    gem_set_length = len(gems_set)

    i = 0
    dist = 0
    cnt = defaultdict(int)
    min_value = gems_length
    answer = [1,gems_length]
    for j in range(gems_length):
        cnt[gems[j]] += 1

        if cnt[gems[j]] == 1:
            dist += 1

        while i <=j and dist == gem_set_length:

            if min_value > j - i + 1:
                min_value = j - i + 1
                answer = [i+1,j+1]

            cnt[gems[i]] -= 1
            if cnt[gems[i]] == 0:
                dist -= 1

            i += 1



    return answer
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
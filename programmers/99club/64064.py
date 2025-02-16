from itertools import product
def solution(user_id, banned_id):
    answer = set()

    ban_possibility = [[] for _ in range(len(banned_id))]

    k = 0
    for ban_id in banned_id:

        for use_id in user_id:
            if len(ban_id) == len(use_id):
                flag = 0
                for i in range(len(ban_id)):
                    if ban_id[i] != "*" and use_id[i] != ban_id[i]:
                        flag = 1
                        break

                if flag == 0:
                    ban_possibility[k].append(use_id)

        k+= 1


    result = list(product(*ban_possibility))


    for m in result:
        if len(set(m)) == len(banned_id):
            answer.add(str(sorted(set(m))))


    print(answer)
    return len(answer)



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))


from itertools import product
def solution(users, emoticons):
    dj = [10, 20, 30, 40]
    graph = [[0] * 4 for _ in range(len(emoticons))]
    for i in range(len(emoticons)):
        for j in range(4):
            graph[i][j]= dj[j]

    # 최대한 많은 사용자가 임플 가입해야함 =>
    combination = list(product(*graph))


    max_sub = 0
    max_value = 0
    plus_sub = 0
    total = 0

    def dfs(V, discount, money):
        nonlocal total, plus_sub
        tmp = 0
        for i in range(len(V)):


            if money > emoticons[i] - int(emoticons[i] * (V[i] / 100)) and discount <= V[i]:

                    money -= emoticons[i] - int(emoticons[i] * (V[i] / 100))
                    tmp += emoticons[i] - int(emoticons[i] * (V[i] / 100))


            elif money <= emoticons[i] - int(emoticons[i] * (V[i] / 100)) and discount <= V[i]:

                plus_sub += 1
                return


        total += tmp
        return


    for i in combination:
        plus_sub = 0
        total = 0
        for user_discount, money in users:
            dfs(i,user_discount,money)



        if max_sub < plus_sub:
            max_sub = plus_sub
            max_value = total

        elif max_sub == plus_sub:

            if max_value < total:
                max_value = total

    return [max_sub,max_value]


print(solution(	[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
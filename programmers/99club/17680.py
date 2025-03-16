# 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자

def solution(cacheSize, cities):
    answer = 0

    cache_tbl = []

    for k in range(len(cities)):
        cities[k] = cities[k].lower()

    print(cities)

    cnt = 0
    i = 0
    while len(cache_tbl) < cacheSize:
        if cities[i] in cache_tbl:

            x = cache_tbl.pop(cache_tbl.index(cities[i]))
            cache_tbl.append(x)
            cnt += 1
            i+= 1

        else:
            cache_tbl.append(cities[i])
            cnt += 5
            i += 1




    for j in range(i,len(cities)):

        if len(cache_tbl) == 0:
            cnt += 5


        elif cities[j] in cache_tbl:

            x = cache_tbl.pop(cache_tbl.index(cities[j]))
            cache_tbl.append(x)
            cnt += 1


        else:

            cache_tbl.pop(0)
            cache_tbl.append(cities[j])
            cnt += 5

    return cnt

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
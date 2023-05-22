def solution(cacheSize, cities):
    cities = [j.lower() for j in cities]
    # print(cities)
    cache = []
    answer = 0
    for i in cities:
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1 # chche hit

        else: # cache miss
            if len(cache) >= cacheSize:
                cache.pop(0)
                cache.append(i)
                answer += 5
            else:
                cache.append(i)
                answer += 5
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
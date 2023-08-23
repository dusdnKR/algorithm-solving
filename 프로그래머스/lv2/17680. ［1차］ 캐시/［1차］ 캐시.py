def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for i, city in enumerate(cities):
        cities[i] = city.lower()
    
    if cacheSize == 0: return len(cities) * 5
            
    for city in cities:
        
        if len(cache) < cacheSize:
            if city not in cache:
                cache.append(city)
                answer += 5
            else:
                answer += 1
                cache.remove(city)
                cache.append(city)
        else:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.append(city)
            else:
                answer += 5
                if cache: del cache[0]
                cache.append(city)
    
    return answer
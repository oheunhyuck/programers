def solution(cacheSize, cities):
    answer = 0
    cache=[]
    cnt=0
    time=0
    temp=0
    if cacheSize==0: return len(cities)*5
    for city in cities:
        city=city.lower()
        f=False
        for i,c in enumerate(cache):
            if c[1]==city:
                temp+=1
                cache[i][0]=temp
                cache.sort(reverse=True)
                time+=1
                f=True
                break
        if f:continue
        if len(cache)<cacheSize:
            temp+=1
            cache.append([temp,city])
            cache.sort(reverse=True)
            time+=5
        else:
            cache.pop()
            temp+=1
            cache.append([temp,city])
            cache.sort(reverse=True)
            time+=5
            
                
            
        
    return time
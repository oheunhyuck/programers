def solution(genres, plays):
    h={}
    answer = []
    
    i=0 
    for g,p in zip(genres,plays):
        if g not in h:
            h[g]=[[i,p]]
        else:
            h[g].append([i,p])
            
        i+=1
    s=sorted(h.items(), key=lambda x: sum(item[1] for item in x[1]),reverse=True)
    
    for i in s:
        song=i[1]
        song.sort(key= lambda x:x[1],reverse=True)
        if len(song)>=2:
            answer.append(song[0][0])
            answer.append(song[1][0])
        else:
            answer.append(song[0][0])
    return answer
            
    

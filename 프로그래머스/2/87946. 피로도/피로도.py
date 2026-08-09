from itertools import permutations
def solution(k, dungeons):
    m=0
    
    for i in permutations(dungeons,len(dungeons)):
        t=k
        cnt=0
        for j in i:
            
            if(t>=j[0]):
                t-=j[1]
                cnt+=1
        m=max(m,cnt)
    
    answer = -1
    return m
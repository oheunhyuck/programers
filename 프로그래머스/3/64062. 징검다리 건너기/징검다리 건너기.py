def binary_search(s,e,stones,k,t):
    if s>e: return s
    m= (s+e) //2
    if is_possible(t,k,stones[m]):
        
        return binary_search(m+1,e,stones,k,t)
    else:
        return binary_search(s,m-1,stones,k,t)
    
def is_possible(stones,k,m):
    cnt=0
    f=False
    for s in stones:
        if s<=m :
            f=True
            cnt+=1
        
        elif s>m and f:
            if cnt>=k:return False
            cnt=0
            f=False
    if cnt>=k:return False
    return True


def solution(stones, k):
    t=sorted(stones)
    
    return t[binary_search(0,len(stones)-1,t,k,stones)]
    
    
    
    
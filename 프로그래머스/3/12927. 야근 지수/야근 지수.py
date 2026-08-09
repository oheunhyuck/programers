import heapq
def solution(n, works):
    if sum(works)<=n:return 0
    h=[]
    s=0
    for i in works:
        heapq.heappush(h,-i)
    for _ in range(n):
        x=heapq.heappop(h)
        heapq.heappush(h,x+1)
    for i in h:
        s+=i**2
    return s
        
    
    
    
    return answer
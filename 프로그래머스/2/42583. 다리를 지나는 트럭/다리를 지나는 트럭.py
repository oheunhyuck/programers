from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    w=0
    t=deque(truck_weights)
    c=deque([])
    while t:
        if t[0]+w <= weight:
            k=t.popleft()
            w+=k
            c.append([k,bridge_length])
        p=0
        for i in range(len(c)):
            if c[i][1]<=1:
                p+=1
                
            else:
                c[i][1]-=1
        for _ in range(p):
            w-=c.popleft()[0]
            
                
            
            
            
            
        
         
        answer+=1
        
        
    answer+=bridge_length
    
        
    return answer
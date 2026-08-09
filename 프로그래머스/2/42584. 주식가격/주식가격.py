from collections import deque

def solution(prices):
    r=[0]*len(prices)
    s=[]
    answer=[]
    for i,j in enumerate(prices):
        if(not s or j>=s[-1][1]):
            s.append((i,j))
        else:
            while s:
                if(s[-1][1]>j):
                    k=s.pop()
                    r[k[0]]=i-k[0]
                else:
                    
                    break
            s.append((i,j))
    while s:
        x=s.pop()
        r[x[0]]=len(prices)-x[0]-1
    for i in r:
        answer.append(i)
                    
                
    
        
        
    
    
    return answer
answer = []
def dfs(n,r,t,v):
    
    f=True
    
    for i in v:
        if not i:f=False
    if f:answer.append(r.copy())
    for i,j in enumerate(t):
        if v[i]==False and j[0]==n:
            r.append(j[1])
            v[i]=True
            dfs(j[1],r,t,v)
            r.pop()
            v[i]=False
        
    
        
        
    
        
            
def solution(tickets):
    v=[False]*len(tickets)
    dfs("ICN",["ICN"],tickets,v)
    answer.sort()
    return answer[0]
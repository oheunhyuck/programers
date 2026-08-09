cnt=0
def dfs(wires,v,n):
    global cnt
    
    for i in wires:
        if(i[0]==n and i[1] not in v):
            t=v.copy()
            t.add(i[1])
            cnt+=1
            
            dfs(wires,t,i[1])
            
            
        if(i[1]==n and i[0] not in v):
            t=v.copy()
            t.add(i[0])
            cnt+=1
            dfs(wires,t,i[0])
            
    
def solution(n, wires):
    global cnt
    answer=[]
    
    for i in wires:
        t = [w for w in wires if w != i]
        cnt=1
        v=set()
        v.add(i[0])
        dfs(t,v,i[0])
        k=cnt
        v=set()
        v.add(i[1])
        cnt=1
        dfs(t,v,i[1])
        answer.append(abs(k-cnt))
        
    
    return min(answer)

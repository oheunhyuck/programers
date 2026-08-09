def dfs_(graph,i,infected,type_,v):
    infected[i]=True
    v.add(i)
    for b,t in graph[i]:
        if type_==t and b not in v:
            dfs_(graph,b,infected,type_,v)
            
        
    

def dfs(k,infected,graph,type_,ans):
        if k==0:
            cnt=0
            for i in range(1,len(infected)):
                if infected[i]==True:cnt+=1
            ans.append(cnt)
                
            return
        temp=infected.copy()
        for i in range(1,len(infected)):
            if infected[i]==True:
                v=set()
                dfs_(graph,i,infected,type_,v)
                
        dfs(k-1,infected,graph,1,ans)
        dfs(k-1,infected,graph,2,ans)
        dfs(k-1,infected,graph,3,ans)
        infected[:]=temp
        
        
        
def solution(n, infection, edges, k):
    answer = 0
    infected=[False]*(n+1)
    infected[infection]=True
    graph=[[] for _ in range(n+1)]
   
    for a,b,t in edges:
        graph[a].append((b,t))
        graph[b].append((a,t))
    
    ans=[]
    dfs(k,infected,graph,1,ans)
    dfs(k,infected,graph,2,ans)
    dfs(k,infected,graph,3,ans)
    return max(ans)
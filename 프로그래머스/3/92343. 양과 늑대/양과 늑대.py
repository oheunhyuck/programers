ans=1
def dfs(cur,info,s,parents):
    global ans
    ans=max(ans,s)
    
    for i in range(len(info)):
        if info[i]==0:
            eat=get(i,parents,0,info,[])
            temp=len(eat)
            
            if cur>temp:
                
            
                info[i]=-1
                
                for e in eat:
                    info[e]=-1
                dfs(cur+1-temp,info,s+1,parents)
                for e in eat:
                    info[e]=1
                info[i]=0
                
        
   


def get(i,parents,w,info,t):
    if i==0: return t
    if info[i]==1:
        t.append(i)
        
    return get(parents[i],parents,w,info,t)
    
def solution(info, edges):
    global ans
    parents=[-1]*(len(info))
    cur=1
    info[0]=-1
    s=1
    for p,c in edges:
        parents[c]=p
    dfs(cur,info,s,parents)
    return ans
       

        
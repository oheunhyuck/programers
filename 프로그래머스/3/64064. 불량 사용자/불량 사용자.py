def dfs(k,path,ans,ban):
    if k==len(ban):
        ans.add(frozenset(path))
        return
    for i in ban[k]:
        if i not in path:
            path.add(i)
            dfs(k+1,path,ans,ban)
            path.remove(i)
        
def is_same(a,b):
    if len(a)!=len(b):return False
    for i,j in zip(a,b):
        if i!=j and i!="*" and j!="*":return False
    return True
        
        
def solution(user_id, banned_id):
    
    ban=[[] for _ in range(len(banned_id))]
    k=0
    
    for b in banned_id:
        
        
        for u in user_id:
            if is_same(b,u):
                ban[k].append(u)
        k+=1
    ans=set()
    path=set()
    dfs(0,path,ans,ban)
    return len(ans)
            
    
    return answer
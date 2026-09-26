def win(a,b):
    for i in range(len(a)-1,-1,-1):
        if a[i]>b[i]:return a
        elif b[i]>a[i]:return b
    return a
def dfs(round_,left,trace,ans,info,point):
    if round_==10:
        ans.append((point,trace[:]+[left]))
        return
    if info[round_]<left:
        trace.append(info[round_]+1)
        
        
        dfs(round_+1,left-(info[round_]+1),trace,ans,info,point+10-round_)
        trace.pop()
    trace.append(0)
    if info[round_]==0:
        dfs(round_+1,left,trace,ans,info,point)
    else:dfs(round_+1,left,trace,ans,info,point-(10-round_))
    trace.pop()
    
def solution(n, info):
    answer = []
    ans=[]
    
    dfs(0,n,[],ans,info,0)
    ans.sort(reverse=True)
    
    if ans[0][0]<=0:return [-1]

    p=ans[0][0]
    for point,trace in ans:
        if point!=p:break
        answer.append(trace)
   
    l=answer[0]
    for i in range(1,len(answer)):
        l=win(l,answer[i])
    return l
    
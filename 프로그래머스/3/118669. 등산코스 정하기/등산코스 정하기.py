import heapq 

def solution(n, paths, gates, summits):
    
    cost=[ 10000001]*(n+1)
    board=[[] for _ in range(n+1)]
    hq=[]
    ans=[50001,10000001]
    target=set()
    for e in summits:
        target.add(e)
    
    for s in gates:
        hq.append([0,s])
        cost[s]=0
    for i,j,w in paths:
        board[i].append([j,w])
        board[j].append([i,w])
    while hq:
        c,cur=heapq.heappop(hq)
        if cost[cur]<c:continue
        if cur in target:
            if c<ans[1]:
                ans[0]=cur
                ans[1]=c
            elif c==ans[1]  and cur<ans[0]:
                ans[0]=cur
                
            continue
        for j,w in board[cur]:
            nc=max(w,c)
            if nc<cost[j]:
                cost[j]=nc
                heapq.heappush(hq,[nc,j])
    return ans
            
        
        
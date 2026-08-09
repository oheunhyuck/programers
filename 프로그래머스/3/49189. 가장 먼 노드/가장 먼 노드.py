import heapq
def solution(n, edge):
    INF=1e8
    v=[False]*(n+1)
    distance=[INF]*(n+1)
    distance[1]=0
    graph=[[] for _ in  range(n+1)]
    for u,w in edge:
        graph[u].append([1,w])
        graph[w].append([1,u])
    q=[]
    heapq.heappush(q,[0,1])
    while q:
        d,i=heapq.heappop(q)
        for e in graph[i]:
            
            j=e[1]
            if v[j]==False:
                distance[j]=min(distance[j],distance[i]+1)
                v[j]=True
                heapq.heappush(q,[distance[j],j])
    distance.sort(reverse=True)
    ans=distance[1:]
    temp=ans[0]
    cnt=0
    for i in ans:
        if i!=temp:break
        cnt+=1
    return cnt
            
    
   
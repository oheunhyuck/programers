import heapq
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    dist=[1e9]*(n+1)
    hq=[]
    dist[destination]=0
    hq.append((0,destination))
    while hq:
        d,cur=heapq.heappop(hq)
        if dist[cur]<d:continue
        for b in graph[cur]:
            k=dist[cur]+1
            if k<dist[b]:
                dist[b]=k
                heapq.heappush(hq,(k,b))
    ans=[]
    for i in sources:
        if dist[i]==1e9:ans.append(-1)
        else:ans.append(dist[i])
        
    return ans
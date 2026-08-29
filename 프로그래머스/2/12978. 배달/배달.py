import heapq
def solution(N, road, K):
    answer = 0
    distance=[1e9]*(N+1)
    distance[1]=0
    graph=[[] for _ in range(N+1)]
    hq=[(0,1)]
    for a,b,c in road:
        graph[a].append((c,b))
        graph[b].append((c,a))
        
    while hq:
        d,cur=heapq.heappop(hq)
        if d>distance[cur]:continue
        
        for w,n in graph[cur]:
            if w+d<distance[n]:
                distance[n]=w+d
                heapq.heappush(hq,(w+d,n))
    cnt=0
    for d in distance:
        if d<=K:cnt+=1
    return cnt
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
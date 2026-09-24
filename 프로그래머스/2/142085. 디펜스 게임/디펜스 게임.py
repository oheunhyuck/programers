import heapq
def solution(n, k, enemy):
    protect_enemy=[]
    for i in range(len(enemy)):
        if n>=enemy[i]:
            heapq.heappush(protect_enemy,-enemy[i])
            n-=enemy[i]
        else:
            f=True
            while  n<enemy[i] and k>0:
                if not protect_enemy:
                
                    k-=1
                    f=False
                    break
                    continue
                if -protect_enemy[0]>enemy[i]:
                    x=-heapq.heappop(protect_enemy)
                    n+=x
                    k-=1
                else:
                    f=False
                    k-=1
                    break
            if f:
                if n>=enemy[i]:
                    heapq.heappush(protect_enemy,-enemy[i])
                    n-=enemy[i]
                else:
                    return i
                
                
    return len(enemy)
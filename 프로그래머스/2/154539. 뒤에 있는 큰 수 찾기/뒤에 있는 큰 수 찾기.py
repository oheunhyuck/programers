import heapq
def solution(numbers):
    answer = [-1]*(len(numbers))
    hq=[]
    for i,n in enumerate(numbers):
        while hq:
            if n>hq[0][0]:
                x=heapq.heappop(hq)
                answer[x[1]]=n
            else:break
                
        heapq.heappush(hq,[n,i])
    return answer
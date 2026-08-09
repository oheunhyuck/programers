def dfs(i,cards,v,k,cycle):
    v[i]=True
    cycle[k].append(i)
    if v[cards[i-1]]==False:
        dfs(cards[i-1],cards,v,k,cycle)
    
def solution(cards):
    answer = 0
    v=[False]*(len(cards)+1)
    cycle=[[] for _ in range(len(cards)+1)]
    for i in range(1,len(cards)+1):
        if v[i]==False:
            dfs(i,cards,v,i,cycle)
    cycle.sort(reverse=True,key=lambda x : len(x))
    
    return len(cycle[0])*len(cycle[1])
    return answer
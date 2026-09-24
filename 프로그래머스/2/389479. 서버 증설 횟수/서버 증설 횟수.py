from collections import deque
def solution(players, m, k):
    answer = 0
    running_server=0
    runtime=deque([])
    ans=0
    
    for i in range(24):
        player=players[i]
        need_server=player//m
        if running_server<need_server:
            ans+=need_server-running_server
            runtime.append([i,need_server-running_server])
            running_server=need_server
            
        if (runtime) and i-runtime[0][0]==k-1:
            running_server-=runtime.popleft()[1]
    return ans
        
        
            
        
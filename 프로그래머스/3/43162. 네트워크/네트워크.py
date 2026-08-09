def dfs(n,v,com,computers):
    v[n]=True
    if n in com:
        com.remove(n)
    for i in range(len(v)):
        if(computers[n][i]==1 and v[i]==False):
            dfs(i,v,com,computers)
            v[n]=False
                
    
def solution(n, computers):
    t=[i for i in range(n)]
    com=set(t)
    cnt=0
    while com:
        cnt+=1
        c=com.pop()
        v=[False]*(n)
        dfs(c,v,com,computers)
    answer = 0
    return cnt
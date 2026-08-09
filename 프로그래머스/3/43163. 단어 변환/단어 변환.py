def check(a,b):
    cnt=0
    for i,j in zip(a,b):
        if i!=j:cnt+=1
    if cnt==1:return True
    return False
def dfs(n,words,v,t,c,answer):
    if n==t:answer.append(c)
    
    for i,j in enumerate(words):
        if v[i]==False and check(n,j):
            v[i]=True
            dfs(j,words,v,t,c+1,answer)
            v[i]=False
    
        
def solution(begin, target, words):
    answer = []
    v=[False]*len(words)
    dfs(begin,words,v,target,0,answer)
    if not answer:return 0
    return min(answer)
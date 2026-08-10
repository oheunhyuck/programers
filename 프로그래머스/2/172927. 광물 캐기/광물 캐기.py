from itertools import permutations
from collections import Counter
def dfs(counter,path,n,u):
    if len(path)==n:
        u.append(path[:])
        return
    for k in counter:
        if counter[k]>0:
            path.append(k)
            counter[k]-=1
            dfs(counter,path,n,u)
            counter[k]+=1
            path.pop()
            
def solution(picks, minerals):
    k=0
    ans=[]
    dict_={"diamond":{"diamond":1,"iron":1,"stone":1 }, "iron":{"diamond":5,"iron":1,"stone":1 } ,"stone":{"diamond":25,"iron":5,"stone":1 }}
    pp=[]
    for _ in range(picks[0]):
        pp.append("diamond")
    for _ in range(picks[1]):
        pp.append("iron")
    for _ in range(picks[2]):
        pp.append("stone")
    counter=Counter(pp)
    u=[]
    dfs(counter,[],len(pp),u)
    
    for p in u:
        s=0
        k=0
        f=False
        for d in p:
            for _ in range(5):
                s+=dict_[d][minerals[k]]
                k+=1
                if k==len(minerals):
                    ans.append(s)
                    f=True
                    break
            if f:break
        ans.append(s)

                
                
    return min(ans)
    answer = 0
    return answer
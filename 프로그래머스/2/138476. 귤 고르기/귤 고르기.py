from collections import Counter
def solution(p, tangerine):
    answer = 0
    a=[]
    c=Counter(tangerine)
    
    for k in c:
        a.append((c[k],k))
    a.sort(reverse=True)
    cnt=0
    s=0
    for c,k in a:
        s+=c
        cnt+=1
        if s>=p:
            break
    return cnt
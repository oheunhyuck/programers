from collections import Counter
from collections import deque
def solution(priorities, location):
    answer = 0
    c=Counter(priorities)
    dq=deque([(i,priorities[i]) for i in range(len(priorities))])
    cur=0
    while dq:
        x=dq.popleft()
        p=x[1]+1
        f=True
        while p<=max(priorities):
            if(c[p]>0):
                dq.append(x)
                f=False
                break
            p+=1
        
        
        if f:
            c[x[1]]-=1
            cur+=1 
            if location==x[0]:
                answer=cur
        
    
    return answer
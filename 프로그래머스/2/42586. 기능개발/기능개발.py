from collections import deque

def solution(progresses, speeds):
    answer = []
    dq=deque(progresses)
    s=deque(speeds)
    
    
    while dq:
        x=dq[0]
        if(x>=100):
            cnt=0
            
            while dq:
                    x=dq[0]
                    if(x>=100):
                        cnt+=1
                        dq.popleft()
                        s.popleft()
                    else:break
            answer.append(cnt)
        for i in range(len(dq)):
            dq[i]+=s[i]
            

        
        
    return answer
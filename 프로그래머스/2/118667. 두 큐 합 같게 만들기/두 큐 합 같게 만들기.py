from collections import deque


        
def solution(queue1, queue2):
    answer = 0
    q1_sum=sum(queue1)
    q2_sum=sum(queue2)
    
    
    total_len=len(queue1)+len(queue2)
    queue1=[(i,queue1[i],1) for i in range(len(queue1))]
    queue2=[(i,queue2[i],2) for i in range(len(queue2))]
    q1=deque(queue1)
    
    q2=deque(queue2)
    
    
    cnt=0
    v=set()
    while True:
        if len(v)==total_len:return -1
    
        
        if q1_sum<q2_sum:
            i,x,t=q2.popleft()
            v.add((i,x,t))
            q1.append((i,x,t))
            q1_sum+=x
            q2_sum-=x
            
            cnt+=1
            
        elif q1_sum>q2_sum:
            i,x,t=q1.popleft()
            v.add((i,x,t))
            q2.append((i,x,t))
            q2_sum+=x
            q1_sum-=x
            cnt+=1
        
        else:
            return cnt
            
    return 
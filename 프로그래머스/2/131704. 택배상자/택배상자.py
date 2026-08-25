
from collections import deque
def solution(order):
    cnt=0
    sub_container=[]
    cnt=0
    container=[i for i in range(len(order),0,-1)]
    is_in_container={i:True for i in range(1,len(order)+1)}
    for order in order:
        if is_in_container[order]:
            while container:
                box=container.pop()
                is_in_container[box]=False
                if box==order:
                    cnt+=1
                    break
                else:
                    sub_container.append(box)
                
            
        else:
            if not sub_container:return cnt
            if sub_container[-1]==order:
                box=sub_container.pop()
                cnt+=1
            else:
                return cnt
            
        
        
    
    return cnt
from collections import deque
def solution(x, y, n):
    dq=deque([ [x,0]    ])
    v=set()
    while dq:
        a,b=dq.popleft()
        
        if a>y or a in v :continue
        v.add(a)
        if a==y: return b
        dq.append([a+n,b+1])
        dq.append([a*2,b+1])
        dq.append([a*3,b+1])
    return -1
    
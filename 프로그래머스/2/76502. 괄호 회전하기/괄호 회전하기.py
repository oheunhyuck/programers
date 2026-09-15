from collections import deque
def is_corret(dq):
    s1=[]
    dict_={"(":")","[":"]","{":"}"}
    for i in dq:
        if i=="(" or i=="{" or i=="[":s1.append(dict_[i])
        else:
            if len(s1)==0:return False
            x=s1.pop()
            if i!=x:return False
    if len(s1)!=0:return False
    return True
        
    
    
def solution(s):
    answer = -1
    cnt=0
    dq=deque([])
    for c in s:
        dq.append(c)
    for i in range(len(s)):
        if is_corret(dq):cnt+=1
        x=dq.popleft()
        dq.append(x)
        
    return cnt
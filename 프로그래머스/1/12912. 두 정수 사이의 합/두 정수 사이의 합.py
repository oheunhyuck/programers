def solution(a, b):
    answer = 0
    s=0
    temp=a
    a=min(a,b)
    b=max(temp,b)
    
    for i in range(a,b+1):
        s+=i
        
    return s
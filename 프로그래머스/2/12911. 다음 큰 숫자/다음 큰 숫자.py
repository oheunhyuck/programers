def solution(n):
    answer = 0
    next=n
    cnt=0
    for i in bin(n)[2:]:
        if i=="1":cnt+=1
    
    while True:
        next+=1
        cnt_=0
        for i in bin(next)[2:]:
            if i=="1":cnt_+=1
        if cnt==cnt_:return next
        
    return answer
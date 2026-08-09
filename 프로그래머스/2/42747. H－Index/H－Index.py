def solution(citations):
    
    for i in range(10000):
        cnt=0
        for j in citations:
            if(i<=j):cnt+=1
        if(cnt>=i):
            answer=i
        else:break
    return answer
        
    
    
    
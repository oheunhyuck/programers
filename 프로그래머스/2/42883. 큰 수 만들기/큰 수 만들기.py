def solution(number, k):
             
    
    s=[]
    n=len(number)
    t=n-k  
    f=False
    for i,j in enumerate(number):
        if f:
            s.append(j)
            continue
            
        if not s:
            s.append(j)
            
        elif s[-1]>= j:
            s.append(j)
        else:
            while s[-1]<j:
                s.pop()
                if(t-len(s)==n-i):
                    
                    f=True
                    break
                    
                if not s:
                    break
                
                    
            s.append(j)
                
                
            
    return "".join(s[0:t])
        
   

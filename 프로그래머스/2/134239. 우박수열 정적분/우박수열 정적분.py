def solution(k, ranges):
    answer = []
    pos=[]
    i=0
    c=0
    while k!=1:
        pos.append((i,k))
        c+=1
        
        
        if k%2==0:
            k=k//2
        else:
            k=k*3+1
        i+=1
        
        if k==1:
            pos.append((i,k))
            c+=1
        
    for i in ranges:
        a,b=i[0],i[1]
        s=0
        if b>0:
            for x in range(a,b):
                s+=(pos[x][1]+pos[x+1][1])/2
        else:
            if c+b-1>=a:
                
                for x in range(a,c+b-1):
                    s+=(pos[x][1]+pos[x+1][1])/2
                answer.append(s)
            else:
                
                answer.append(-1)
        
        
            
            
        
    return answer
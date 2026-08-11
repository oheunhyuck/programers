def solution(n, stations, w):
    answer = 0
    t=2*w+1
    cnt=0

    
    for i in range(len(stations)) :
        if i ==0:
            k=stations[0]-(w+1)
            
        
            
        else:
            k=(stations[i]-(w+1)) - (stations[i-1]+(w+1))+1
        
        if k>0:
            if k % t==0:
                cnt+=k//t
            else:
                cnt+=(k//t)+1
    if n -(stations[-1]+(w+1))+1 <=0  :return cnt

    if (n -(stations[-1]+(w+1))+1)%t==0:
        cnt+=(n -(stations[-1]+(w+1))+1) //t
        
    else:
        cnt+=(n -(stations[-1]+(w+1))+1) //t  +1
        
    return cnt
            
        

    return answer
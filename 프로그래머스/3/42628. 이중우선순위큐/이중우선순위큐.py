import heapq
def solution(operations):
    answer = []
    hq=[]
    hqq=[]
    dict_={}
    cnt=0
    for i in operations:
        x=i.split(" ")
        o,v=x[0],int(x[1])
        if o=="I":
            heapq.heappush(hq,-int(v))
            heapq.heappush(hqq,int(v))
            if v in dict_:
                dict_[v]+=1
            else:
                dict_[v]=1
            cnt+=1
            
        elif o=="D": 
            if v==1:
                while hq:
                    
                    x= -heapq.heappop(hq)
                    if dict_[x]>=1:
                        cnt-=1
                        dict_[x]-=1
                        break
                
            else:
                while hqq:
                    x=heapq.heappop(hqq)
                    if dict_[x]>=1:
                        cnt-=1
                        dict_[x]-=1
                        break
                    
            
    if cnt>0:
        ma=0
        mi=0
        while hq:
             
                    x= -heapq.heappop(hq)
                    if dict_[x]>=1:
                        ma=x
                        break
        while hqq:
             
                    x= heapq.heappop(hqq)
                    if dict_[x]>=1:
                        
                        mi=x
                        break
            
        return [ma,mi]
    else:
        return [0,0]
        
    
        
    
    return [hq]
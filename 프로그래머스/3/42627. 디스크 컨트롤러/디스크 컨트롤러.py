import heapq

def solution(jobs):
    answer = 0
    s=0
    h=[]
    c=len(jobs)
    jobs=[[j[0],j[1]]+[i] for i,j in enumerate(jobs)]
    heapq.heapify(jobs)
    while jobs or h:
        
        while jobs:
            
                if jobs[0][0]<=s:
                    x=heapq.heappop(jobs)
                    y=[x[1],x[0],x[2]]
                    heapq.heappush(h,y)
                else:break
        if  h:
            x=heapq.heappop(h)
            s+=x[0]
            
            answer+=s-x[1]
        else:
            s+=1
        
            
            

        
    return answer//c
                    
            
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
    
                                    
        
     
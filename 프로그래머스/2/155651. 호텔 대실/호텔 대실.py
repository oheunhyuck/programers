def solution(book_time):
    stay=[]
    max_=0
    book_time.sort()
    
    for i,t in enumerate(book_time):
        start_time,fin_time=t[0],t[1]
        
            
        cnt=0
        for s in stay:
            if start_time<s:
                cnt+=1
            
        max_=max(max_,cnt+1)
        
        temp=int(fin_time[3:])+10
        if temp>=60:
                t=str(int(fin_time[:2])+1)
                
                tt=str(temp-60)
                
                if len(t)==1:
                    t="0"+t
                
                if len(tt)==1:
                    tt="0"+tt
                stay.append(t+":"+tt)
                    
                
        else:
                stay.append(fin_time[:3]+str(temp))
            
    return max_
 
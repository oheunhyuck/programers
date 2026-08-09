from collections import deque
def solution(n, t, m, timetable):
    answer = ''
    wait=deque([])
    p=n*m
    j=0
    timetable.sort()
    take=[0]*n
    bus_time=["09:00"]
    for i in range(1,n):
        a,b =map(int,bus_time[i-1].split(":"))
        if b+t>=60:
            a+=1
            b=b+t-60
            
        else:
            b=b+t
        if a>=10:
            a=str(a)
        else:
            a="0"+str(a)
        if b>=10:
            b=str(b)
        else:
            b="0"+str(b)
        bus_time.append(a+":"+b)
                
                
            
        
        
        
    cnt=-1
    for i,b in enumerate(bus_time):
        while j<len(timetable) and timetable[j]<=b :
            wait.append(1)
            j+=1
        for _ in range(m):
            if len(wait)>0:
                x=wait.popleft()
                take[i]+=1
                cnt+=1
            else:break
    
    
    if take[n-1]<m:return bus_time[i]
    a,b=map(int, timetable[cnt].split(":"))
    if b==0:
        a-=1
        b=59
    else:
        b-=1
    if a>=10:
        a=str(a)
    else:a="0"+str(a)
    if b>=10:
        b=str(b)
    else:b="0"+str(b)
    
    return a+":"+b
    
    return timetable[cnt]
 
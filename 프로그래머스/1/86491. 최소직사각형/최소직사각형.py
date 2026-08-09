def solution(sizes):
    answer = 0
    f=0
    s=0
    t=0
    tt=0
    for i in range(len(sizes)):
        if(sizes[i][0]>f):
            
            s=f
            tt=t
            
            f=sizes[i][0]
            t=sizes[i][1]
            
        elif(sizes[i][0]==f):
            t=min(sizes[i][1],t)
            
            min(sizes[i][1],t)
        elif(sizes[i][0]>s):
            s=sizes[i][0]
            
        if(sizes[i][1]>=f):
            s=f
            tt=t
            
            f=sizes[i][1]
            t=sizes[i][0]
        elif(sizes[i][1]==f):
            t=min(sizes[i][0],t)
        elif(sizes[i][1]>s):
            s=sizes[i][1]
            tt=sizes[i][0]
            
    if s==t or tt==f:return s*f
    for i,j in sizes:
        c=min(i,j)
        if(c>tt):
            tt=c
    return tt*f
        
    
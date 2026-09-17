def solution(dirs):
    answer = 0
    v=set()
    x=0
    
    y=0
    cnt=0
    for d in dirs:
        if d=="U":
            nx=x
            ny=y+1
            if nx>5 or nx<-5 or ny>5 or ny<-5:continue
            
            
            
        elif d=="D":
            nx=x
            ny=y-1
            if nx>5 or nx<-5 or ny>5 or ny<-5:continue
            
        elif d=="R":
            nx=x+1
            ny=y
            if nx>5 or nx<-5 or ny>5 or ny<-5:continue
        elif d=="L":
            nx=x-1
            ny=y
            if nx>5 or nx<-5 or ny>5 or ny<-5:continue
        if ((x,y),(nx,ny)) not in v:cnt+=1
        v.add(((x,y),(nx,ny)))
        v.add(((nx,ny),(x,y)))
        x=nx
        y=ny
        
    return cnt
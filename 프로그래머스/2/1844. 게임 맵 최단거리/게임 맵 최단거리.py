from collections import deque

def solution(maps):
    dq=deque([[1,1,1]])
    v={(1,1)}
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while dq:
        p=dq.popleft()
        for i in range(4):
            x,y=p[0]+dx[i],p[1]+dy[i]
            if( 1<=x and x<=len(maps) and y>=1 and y<=len(maps[0])):
                
                if((x,y) not in v and maps[x-1][y-1]!=0):
                
                    if(x==len(maps) and y==len(maps[0])):
                        return p[2]+1
                    v.add((x,y))
                    dq.append([x,y,p[2]+1])
            
        
        
        
    
    
    return -1
from collections import deque
def solution(maps):
    
    s=[0,0]
    e=[0,0]
    l=[0,0]
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x]=="S":
                s=[y,x]
            if maps[y][x]=="E":
                e=[y,x]
            if maps[y][x]=="L":
                l=[y,x]
    dq=deque([[s[0],s[1],0]])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    cnt=0
    f=True
    v=set()
    while dq:
        y,x,c=dq.popleft()
        
        if maps[y][x]=="L":
            cnt+=c
            f=False
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=len(maps[0]) or ny<0 or ny>=len(maps) or maps[ny][nx]=="X" or (ny,nx) in v:continue
            dq.append([ny,nx,c+1])
            v.add((ny,nx))
    if f:return -1
    dq=deque([[l[0],l[1],0]])
    
    
    f=True
    v=set()
    while dq:
        y,x,c=dq.popleft()
        
        if maps[y][x]=="E":
            cnt+=c
            f=False
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=len(maps[0]) or ny<0 or ny>=len(maps) or maps[ny][nx]=="X" or (ny,nx) in v:continue
            dq.append([ny,nx,c+1])
            v.add((ny,nx))
    if f:return -1
            
        
    
    return cnt

from collections import deque
def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
def bfs(maps,start,end):
    v=set()
    v.add((start[0],start[1]))
    q=deque([[start[0],start[1],0]])
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        t=q.popleft()
        y,x,cnt=t[0],t[1],t[2]
        if y==end[0] and x==end[1]:return cnt
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny<0 or ny>4 or nx<0 or nx>4 or maps[ny][nx]=="X" or (ny,nx) in v:continue
            v.add((ny,nx))
            q.append([ny,nx,cnt+1])
            
    
    
    return 1000
        
    
def solution(places):
    answer = []
    for place in places:
        sit=[]
        f=True
        
        for y in range(5):
            for x in range(5):
                if place[y][x]=="P":sit.append([y,x])
        for i in range(len(sit)):
            for j in range(i+1,len(sit)):
                if distance(sit[i],sit[j])<=2:
                    if bfs(place,sit[i],sit[j])<=2:
                        answer.append(0)
                        f=False
                        break
            if not f:break
        if f:answer.append(1)
                        
    
    
    return answer
import sys
sys.setrecursionlimit(10**6)
min_x=1000
max_x=-1
cnt=0
def add(count,min_x,max_x,cnt):
    for i in range(min_x,max_x+1):
        count[i]+=cnt
def dfs(land,cur_y,cur_x,v):
    global min_x
    global max_x
    global cnt
    v.add((cur_y,cur_x))
    min_x=min(cur_x,min_x)
    max_x=max(cur_x,max_x)
    cnt+=1
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    for i in range(4):
        ny=cur_y+dy[i]
        nx=cur_x+dx[i]
        if ny<0 or nx<0 or ny>=len(land) or nx>=len(land[0]) or (ny,nx) in v or land[ny][nx]==0: continue
        
        
        dfs(land,ny,nx,v)
        
    
def solution(land):
    global min_x,max_x,cnt
    ans=[]
    v=set()
    count=[0]*(len(land[0]))
    for y in range(len(land)):
        for x in range(len(land[0])):
            if (y,x) not in v and land[y][x]==1:
                
                dfs(land,y,x,v)
                add(count,min_x,max_x,cnt)
                ans.append(cnt)
                min_x=1000
                max_x=-1
                cnt=0
                
                
    return max(count)
import sys
sys.setrecursionlimit(10**6)
f=0
cnt=0
def out_one(v,y,x,storage,k):
    global cnt
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny<0 or ny>=len(v) or nx<0 or nx>=len(v[0]) or v[ny][nx]==False or storage[ny][nx]!=k:continue
            
            cnt+=1  
            v[ny][nx]=False
            out_one(v,ny,nx,storage,k)
            
def dfs(v,y,x,temp_v,storage,k):
    global f,cnt
    temp_v.add((y,x))
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    if y==0 or y==len(v)-1 or x==0 or x==len(v[0])-1:
        f=1
    
        return

    
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if v[ny][nx]==False and (ny,nx) not in temp_v:
            dfs(v,ny,nx,temp_v,storage,k)
def out_all(storage,k,v):
    global cnt
    k=k[0]
    for y in range(len(storage)):
        for x in range(len(storage[0])):
            if storage[y][x]==k and v[y][x]==True:
                v[y][x]=False
                cnt+=1
def out_line(storage,k,v):
    global cnt,f
    temp=[]
    for y in range(len(storage)):
        for x in range(len(storage[0])):
            if storage[y][x]==k and v[y][x]:
                f=0
                dfs(v,y,x,set(),storage,k)
                if f==1:
                    
                    temp.append([y,x])
    for y,x in temp:
        cnt+=1
        v[y][x]=False
                    
                
def solution(storage, requests):
    answer = 0
    v=[[True]*len(storage[0]) for _ in range(len(storage))]
    for r in requests:
        if len(r)==2:
            out_all(storage,r,v)
        else:
            out_line(storage,r,v)
    
    
    return  len(storage)*len(storage[0])-cnt
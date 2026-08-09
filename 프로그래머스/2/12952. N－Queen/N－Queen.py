cnt=0
def dfs(maps,x,n):
    global cnt
    
    if x>=n: 
        cnt+=1
        return
    for y in range(n):
        if maps[y][x]==True:
            temp=[ k[:] for k in maps]
            for nx in range(x+1,n):
                maps[y][nx]=False
            nx=x+1
            ny=y-1
            while nx<n and ny>=0:
                maps[ny][nx]=False
                nx+=1
                ny-=1
            nx=x+1
            ny=y+1
            while nx<n and ny<n:
                maps[ny][nx]=False
                nx+=1
                ny+=1
            
            dfs(maps,x+1,n)
            maps=temp
def solution(n):
    global cnt
    answer = 0
    maps=[[True]*n for _ in range(n)]
    dfs(maps,0,n)
            
    return cnt
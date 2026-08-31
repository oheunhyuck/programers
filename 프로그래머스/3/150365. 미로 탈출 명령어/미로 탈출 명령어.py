from collections import deque
import sys
sys.setrecursionlimit(10**6)
anss=""
f=False
def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
def dfs(cur,cnt,k,ans,end,n,m,trace):
    global anss
    global f
    if f:return
    if distance(cur,end)>k-cnt:return
    if (k-cnt-distance(cur,end)) % 2 ==1:return
    if cnt==k:
        if cur[0]==end[0] and cur[1]==end[1]:
            f=True
            anss=trace
            return
        return
    dx=[0,-1,1,0]  
    dy=[1,0,0,-1]
    for i in range(4):
        ny=cur[0]+dy[i]
        nx=cur[1]+dx[i]
        if ny<0 or ny>=n or nx<0 or nx>=m:continue
        if i==0:
            dfs([ny,nx],cnt+1,k,ans,end,n,m,trace+"d")
        elif i==1:
            dfs([ny,nx],cnt+1,k,ans,end,n,m,trace+"l")
        elif i==2:
            dfs([ny,nx],cnt+1,k,ans,end,n,m,trace+"r")
        elif i==3:
            dfs([ny,nx],cnt+1,k,ans,end,n,m,trace+"u")
        
        

def solution(n, m, x, y, r, c, k):
    ans = []
    start=[x-1,y-1]
    end=[r-1,c-1]
    
    dfs(start,0,k,ans,end,n,m,"")
    
    
    if not f:return "impossible"
    return anss
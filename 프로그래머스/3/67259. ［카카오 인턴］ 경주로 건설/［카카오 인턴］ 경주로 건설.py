import sys
sys.setrecursionlimit(10**6)
answer=[]
def dfs(board,cur,cost,direction,v,best):
    global answer
    
    v.add(tuple(cur))
    n=len(board[0])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]  #오 왼 위 아래
    d=["r","l","u","d"]
    dd={"r":0,"l":1,"u":2,"d":3}
    if direction!="s":
        if best[dd[direction]][cur[0]][cur[1]]<=cost:
            v.remove(tuple(cur))
            return
        else:best[dd[direction]][cur[0]][cur[1]]=cost
    
    if cur[0]==n-1 and cur[1]==n-1:
        answer.append(cost)
        v.remove(tuple(cur))
        return
    for i in range(4):
        nx=cur[1]+dx[i]
        ny=cur[0]+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n or board[ny][nx]==1 or (ny,nx) in v:continue
        
        if direction=="s" :
            
            dfs(board,[ny,nx],cost+100,d[i],v,best)
       
        elif  direction==d[i]:
            dfs(board,[ny,nx],cost+100,direction,v,best)
            
        else:
            dfs(board,[ny,nx],cost+600,d[i],v,best)
    v.remove(tuple(cur))
            
    
    
def solution(board):
    best=[[[10**6]*len(board) for _ in range(len(board))] for _ in range(4)]
    dfs(board,[0,0],0,"s",set(),best)
    

    return sorted(answer)[0]
import sys
sys.setrecursionlimit(10**6)
def is_same(a,b):
    for i,j in zip(a,b):
        if i!=j:return False
    return True

def check(k,e):
    for p in range(len(k)):
        dx=-k[p][0]
        dy=-k[p][1]
        temp=[l[:] for l in k]
        for t in range(len(temp)):
            temp[t][0]+=dx
            temp[t][1]+=dy
        temp.sort()
        for _ in range(4):
            for t in range(len(temp)):
                a=temp[t][0]
                b=temp[t][1]
                temp[t][0]=b
                temp[t][1]=-a
            temp.sort()
            if is_same(temp,e):return True
    return False
    
def dfs(game_board,v,trace,sy,sx,cur_y,cur_x):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    v.add((cur_y,cur_x))
    trace.append([cur_y-sy,cur_x-sx])
    
    for i in range(4):
        ny=cur_y+dy[i]
        nx=cur_x+dx[i]
        if ny<0 or nx<0 or ny>=len(game_board) or nx>=len(game_board[0]) or game_board[ny][nx]==1 or (ny,nx) in v:continue
        dfs(game_board,v,trace,sy,sx,ny,nx)
def dfs_(game_board,v,trace,sy,sx,cur_y,cur_x):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    v.add((cur_y,cur_x))
    trace.append([cur_y-sy,cur_x-sx])
    
    for i in range(4):
        ny=cur_y+dy[i]
        nx=cur_x+dx[i]
        if ny<0 or nx<0 or ny>=len(game_board) or nx>=len(game_board[0]) or game_board[ny][nx]==0 or (ny,nx) in v:continue
        dfs_(game_board,v,trace,sy,sx,ny,nx)
    
def solution(game_board, table):
    v=set()
    ans=0
    used=set()
    v2=set()
    empty=[[] for _ in range(7)]
    key=[[] for _ in range(7)]
    
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            if (y,x) not in v and game_board[y][x]==0:
                trace=[]
                dfs(game_board,v,trace,y,x,y,x)
                cnt=len(trace)
                empty[cnt].append(sorted(trace))
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            if (y,x) not in v2 and table[y][x]==1:
                trace=[]
                dfs_(table,v2,trace,y,x,y,x)
                cnt=len(trace)
                key[cnt].append(sorted(trace))
    for i in range(1,7):
        for k in key[i]:
            for j,e in enumerate(empty[i]):
                if (i,j) in used:continue
                if check(k,e):
                
                    ans+=i
                    used.add((i,j))
                    break
                
                
    return ans
                
            
            
    
                
                
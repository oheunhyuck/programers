def is_in(x,y,key):
    if x>key[0][0] and x<key[1][0] and y> key[0][1] and y< key[1][1]:return True
    return False
def dfs(x,y,cnt,v,key,board,tx,ty,ans):
    if x==tx and y==ty:
        
        ans.append(cnt)
        return
    
    for k in key:
        if is_in(x,y,k):return
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=102 or ny>=102 or board[nx][ny]==False or v[nx][ny]:continue
        v[nx][ny]=True
        dfs(nx,ny,cnt+1,v,key,board,tx,ty,ans)
        
        v[nx][ny]=False

def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX*=2
    characterY*=2
    itemX*=2
    itemY*=2
    answer = 0
    key=[]
    board=[[False]*102 for _ in range(102)]
    v=[[False]*102 for _ in range(102)]
    for x1,y1,x2,y2 in rectangle:
        x1*=2
        y1*=2
        x2*=2
        y2*=2
        
        key.append([(x1,y1),(x2,y2)])
        for x in range(x1,x2+1):
            board[x][y1]=True
            board[x][y2]=True
        for y in range(y1,y2+1):
            board[x1][y]=True
            board[x2][y]=True
    ans=[]
    v[characterX][characterY]=True
    dfs(characterX,characterY,0,v,key,board,itemX,itemY,ans)   
    return min(ans) //2
from collections import deque
def solution(board):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    v=set()
    answer = 0
    q=deque([])
    goal=[]
    pos=[]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]=="R":
                pos=[y,x]
            if board[y][x]=="G":
                goal=[y,x]
    q.append([pos,0])
    v.add(tuple(pos))
    while q:
        x=q.popleft()
        pos,c=x[0],x[1]
        if pos==goal: return c
        for i in range(4):
            nx=dx[i]+pos[1]
            ny=dy[i]+pos[0]
            if nx >= len(board[0]) or nx<0 or ny<0 or ny>=len(board):continue
            if board[ny][nx]=="D":continue
        #-> 
            if i==0:
                while True:
                    if nx >= len(board[0]) or nx<0 or ny<0 or ny>=len(board):break
                    if board[ny][nx]=="D":break
                    nx+=1
                nx-=1
        #<- 
            if i==1:
                while True:
                    if nx >= len(board[0]) or nx<0 or ny<0 or ny>=len(board):break
                    if board[ny][nx]=="D":break
                    nx-=1
                nx+=1
            
        #^
            if i==3:
                while True:
                    if nx >= len(board[0]) or nx<0 or ny<0 or ny>=len(board):break
                    if board[ny][nx]=="D":break
                    ny-=1
                ny+=1
            
            if i==2:
                while True:
                    if nx >= len(board[0]) or nx<0 or ny<0 or ny>=len(board):break
                    if board[ny][nx]=="D":break
                    ny+=1
                ny-=1
            if (ny,nx) not in v:
                q.append([[ny,nx],c+1])
                v.add((ny,nx))
            
        
        
            
        
    return -1
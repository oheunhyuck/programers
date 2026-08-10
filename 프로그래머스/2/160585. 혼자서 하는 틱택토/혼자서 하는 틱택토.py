
def solution(board):
    a=0
    b=0
    for y in board:
        for x in y:
            if x=="O":
                a+=1
            elif x=="X":
                b+=1
    if a-b>=2 or b-a>=1:return 0
    cnt=0
    k=""
    
    for y in range(3):
        c=board[y][0]
        if c==".":continue
        f=True
        for x in range(3):
            if board[y][x]!=c:f=False
        if f:
            if k!="" and k!=c:return 0
            k=c
            cnt+=1
    for x in range(3):
        c=board[0][x]
        if c==".":continue
        f=True
        for y in range(3):
            if board[y][x]!=c:f=False
        if f:
            if k!="" and k!=c:return 0
            k=c
            cnt+=1
    
    if board[1][1]!="." and board[1][1]==board[0][0] and board[1][1]==board[2][2]:
        if k!="" and k!=board[1][1]:return 0
        k=board[1][1]
        cnt+=1
    if board[1][1]!="." and board[1][1]==board[0][2] and board[1][1]==board[2][0]:
        if k!="" and k!=board[1][1]:return 0
        k=board[1][1]
        cnt+=1
    
    if cnt==1 and k=="O" and a!=b+1:return 0
    if cnt==1 and k=="X" and a!=b:return 0
    
    return 1
                
    answer = -1
    return answer
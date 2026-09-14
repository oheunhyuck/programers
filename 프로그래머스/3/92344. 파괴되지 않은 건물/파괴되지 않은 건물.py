def solution(board, skill):
    smap=[[0]*len(board[0]) for _ in range(len(board))]
    ans_map=[[0]*len(board[0]) for _ in range(len(board))]
    for ty,y1,x1,y2,x2,a in skill:
        if ty==1:a=-a
        dx1=min(x1,x2)
        dy1=min(y1,y2)
        dx2=max(x1,x2)+1
        dy2=max(y1,y2)+1
        smap[dy1][dx1]+=a
        if dy2<len(board):
            smap[dy2][dx1]-=a
        if dx2<len(board[0]):
            smap[dy1][dx2]-=a
        if dy2<len(board) and dx2<len(board[0]):
            smap[dy2][dx2]+=a
        
        
    for x in range(len(board[0])):
        s=0
        for y in range(len(board)):
            s+=smap[y][x]
            smap[y][x]=s
    cnt=0
    for y in range(len(board)):
        s=0
        for x in range(len(board[0])):
            s+=smap[y][x]
            smap[y][x]=s
            if smap[y][x]+board[y][x]>0:cnt+=1
    return cnt
    
            
            
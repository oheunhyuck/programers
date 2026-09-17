def solution(rows, columns, queries):
    answer = []
    temp=1
    board=[[0]*(columns+1) for _ in range(rows+1)];
    for y in range(1,rows+1):
        for x in range(1,columns+1):
            board[y][x]=temp
            temp+=1
    
    for y1,x1,y2,x2 in queries:
        
        temp=board[y1][x2]
        temp2=board[y2][x2]
        temp3=board[y2][x1]
        k=min(temp,temp2,temp3)
        for x in range(x2,x1,-1):
            board[y1][x]=board[y1][x-1]
            k=min(k,board[y1][x-1])
        
        for y in range(y2,y1+1,-1):
            board[y][x2]=board[y-1][x2]
            k=min(k,board[y-1][x2])
            
        board[y1+1][x2]=temp
        for x in range(x1,x2-1):
            board[y2][x]=board[y2][x+1]
            k=min(k,board[y2][x+1])
        board[y2][x2-1]=temp2
        for y in range(y1,y2-1):
            board[y][x1]=board[y+1][x1]
            k=min(k,board[y+1][x1])
        board[y2-1][x1]=temp3
        
        answer.append(k)
        
        
        
    
        
            
    return answer

def solution(m, n, board):
    answer = 0
    temp=[["*"]*n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            temp[y][x]=board[y][x]
    board=temp

    while True:
        f=True
        d=set()
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x]==board[y][x+1] and board[y][x]==board[y+1][x] and board[y][x]==board[y+1][x+1] and board[y][x]!="*":
                    f=False
                    d.add((y,x))
                    d.add((y+1,x))
                    d.add((y,x+1))
                    d.add((y+1,x+1))
        answer+=len(d)
        
        if f:return answer
        
        for x in range(n):
            s=[]
            for y in range(m):
                if (y,x) not in d:s.append(board[y][x])
            for y in range(m-1,-1,-1):
                if len(s)!=0:board[y][x]=s.pop()
                else:board[y][x]="*"
        
        
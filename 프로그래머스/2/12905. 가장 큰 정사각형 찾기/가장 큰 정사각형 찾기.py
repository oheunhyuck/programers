
def solution(board):
                    
    ans=0   
    if len(board)<2 or len(board[0])<2:return 1
    for y in range(1,len(board)):
        for x in range(1,len(board[0])):
            if board[y][x]==1:
                board[y][x]=min(board[y][x-1],board[y-1][x-1],board[y-1][x])+1
                ans=max(board[y][x],ans)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return ans**2
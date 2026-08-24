def solution(land):
    answer = 0
    for y in range(1,len(land)):
        for x in range(4):
            if x==0:
                land[y][x]+=max(land[y-1][1],land[y-1][2],land[y-1][3])
            if x==1:
                land[y][x]+=max(land[y-1][0],land[y-1][2],land[y-1][3])
            if x==2:
                land[y][x]+=max(land[y-1][1],land[y-1][0],land[y-1][3])
            if x==3:
                land[y][x]+=max(land[y-1][1],land[y-1][2],land[y-1][0])
    return max(land[-1][0],land[-1][1],land[-1][2],land[-1][3])
            
            
            
            
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
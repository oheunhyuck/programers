def solution(n):
    map=[[0]*(i+1) for i in range(n)]
    cnt=0
    s=0
    mode=0
    cur_x,cur_y=0,0
    for j in range(1,n+1):
        s+=j
    while cnt<s:
        if mode==0:
            while cur_y<n and map[cur_y][cur_x]==0:
                cnt+=1
                map[cur_y][cur_x]=cnt
                cur_y+=1
            cur_y-=1
            
            cur_x+=1
            
            mode+=1
            
        if mode==1:
            while cur_x<=cur_y and map[cur_y][cur_x]==0:
                cnt+=1
                map[cur_y][cur_x]=cnt
                cur_x+=1
            cur_x-=1
            
            cur_y-=1
            cur_x-=1
            
            mode+=1
            
        if mode==2:
            while map[cur_y][cur_x]==0:
                cnt+=1
                map[cur_y][cur_x]=cnt
                cur_y-=1
                cur_x-=1
            cur_y+=1
            cur_x+=1
            cur_y+=1
            
            mode=0
    answer=[]
    for i in map:
        for j in i:
            answer.append(j)
    return answer
                
            
                
                
        
        
        
        
        
    answer = []
    return answer
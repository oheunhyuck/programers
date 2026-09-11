def is_remove(x,y,ty,safe_map,ans_map):
    if ty==0:
        safe_map[x][y+1]-=2
        
        if (not 1 in ans_map[x-1][y+1] or is_safe(x-1,y+1,1,safe_map,True)) and (not 0 in ans_map[x][y+1] or is_safe(x,y+1,0,safe_map)) and (not 1 in ans_map[x][y+1] or is_safe(x,y+1,1,safe_map,True)) :
            safe_map[x][y+1]+=2
            return True
        safe_map[x][y+1]+=2
        return False
        
        
    elif ty==1:
        safe_map[x][y]-=1
        safe_map[x+1][y]-=1
        
        if (not 1 in ans_map[x-1][y] or is_safe(x-1,y,1,safe_map,True)) and (not 0 in ans_map[x][y] or is_safe(x,y,0,safe_map))  and (not 1 in ans_map[x+1][y] or is_safe(x+1,y,1,safe_map,True)) and (not 0 in ans_map[x+1][y] or is_safe(x+1,y,0,safe_map)) :
            safe_map[x][y]+=1
            safe_map[x+1][y]+=1
            return True
        safe_map[x][y]+=1
        safe_map[x+1][y]+=1
        return False
        
        
        if ans_map[x+1][y]==1 and safe_map[x+2][y]>=2: return True
        return False
            
        
def is_safe(x,y,ty,safe_map,f=False):
    if x<0:return True
    if ty==0:
        
        
        if y==0:return True
        if safe_map[x][y]>=1:return True
        
        
    elif ty==1:
        if x+1>=len(safe_map):return True
        if f:
            if safe_map[x][y]+safe_map[x+1][y]>=4:return True
        else:
            
            if safe_map[x][y]+safe_map[x+1][y]>=2:return True
    
    return False
    
def solution(n, build_frame):
    answer = []
    safe_map=[[0]*(n+1) for _ in range(n+1)]
    ans_map=[[[]for _ in range(n+1)] for _ in range(n+1)]
    for x,y,ty,o in build_frame:
        if o==0:#삭제
            if is_remove(x,y,ty,safe_map,ans_map):
                ans_map[x][y].remove(ty)
                if ty==0:
                    safe_map[x][y+1]-=2
                elif ty==1:
                    safe_map[x][y]-=1
                    safe_map[x+1][y]-=1
                    
            
        else:#설치
            if is_safe(x,y,ty,safe_map):
                ans_map[x][y].append(ty)
                if ty==0:#기둥
                    safe_map[x][y+1]+=2
                elif ty==1:#보
                    safe_map[x+1][y]+=1
                    safe_map[x][y]+=1
                    
    for dx in range(n+1):
        for dy in range(n+1):
            if len(ans_map[dx][dy])==0:continue
            ans_map[dx][dy].sort()
            for i in ans_map[dx][dy]:
                answer.append([dx,dy,i])
                
    return answer
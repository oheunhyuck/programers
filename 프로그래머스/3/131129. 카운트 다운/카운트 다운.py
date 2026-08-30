from collections import deque
def solution(target):
    answer = []
    points=[]
    dict_={}
    temp=[i+1 for i in range(20)]
    q=deque([ [0,0,0]   ]) #횟수 싱글 불 점수 
    for i in range(1,21):
        if i not in points:
            points.append(i)
        if i*2 not in points:
            points.append(i*2)
        if i*3 not in points:
            points.append(i*3)
    points.append(50)
    f=1e9
    
    bull=[]
    while q:
        x=q.popleft()
        cnt,single_bull,point=x[0],x[1],x[2]
        if point>target or cnt>f:continue
        if point==target:
            f=cnt
            bull.append(single_bull)
            
            
            
            
        for p in points:
        
            if p in temp or p==50:
                if point+p in dict_:
                    
                        
                    if dict_[point+p][0]<cnt+1:
                        continue
                    else:
                        if dict_[point+p][1]<single_bull+1:
                            
                             dict_[point+p]=[cnt+1,single_bull+1]
                            
                             q.append([cnt+1,single_bull+1,point+p])
                            
                else:
                    dict_[point+p]=[cnt+1,single_bull+1]
                    q.append([cnt+1,single_bull+1,point+p])
                        
                
                
                
            else:
                if point+p in dict_:
                    
                        
                    if dict_[point+p][0]<cnt+1:
                        continue
                    else:
                        if dict_[point+p][1]<single_bull:
                            
                             dict_[point+p]=[cnt+1,single_bull]
                            
                             q.append([cnt+1,single_bull,point+p])
                            
                else:
                    dict_[point+p]=[cnt+1,single_bull]
                    q.append([cnt+1,single_bull,point+p])
                
        
        
        
    return [f,max(bull)]
    return answer
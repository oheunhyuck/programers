def rotate(key):
    for k in key:
        for p in k:
            x=p[1]
            y=p[0]
            p[0]=x
            p[1]=-y
            
def solution(key, lock):
    answer = True

    k1=[]
    k2=[]
    k3=[]
    k4=[]
    cnt=0
    for y in range(len(key)):
        for x in range(len(key)):
            if key[y][x]==1:
                t=len(key)-1
                k1.append([y,x])
                k2.append([y,x-t])
                k3.append([y-t,x])
                k4.append([y-t,x-t])
    temp=[k1,k2,k3,k4]
    for y in range(len(lock)):
        for x in range(len(lock)):
            if lock[y][x]==0:
                cnt+=1
    for _ in range(4):
        for y in range(len(lock)):
            for x in range(len(lock)):
                for k in temp:
                    tcnt=0
                    f=True
                    for up in k:
                        nx=x+up[1]
                        ny=y+up[0]
                        if nx<0 or nx>=len(lock) or ny<0 or ny>=len(lock):continue
                        if lock[ny][nx]==1:
                            f=False
                            break
                        tcnt+=1
                    if f:
                        if tcnt==cnt:return True
        rotate(temp)
                
    return False
                        
                
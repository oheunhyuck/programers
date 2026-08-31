def make_y(trace,y,n):
    if len(trace)==n:
        y.append(trace[:])
        return
    trace.append(1)
    make_y(trace,y,n)
    trace.pop()
    trace.append(0)
    make_y(trace,y,n)
    trace.pop()
    
    
    
def solution(beginning, target):
    
    ny=[]
    nx=[]
    make_y([],ny,len(beginning))
    make_y([],nx,len(beginning[0]))
    ans=[]
    for dy in ny:
       for dx in nx: 
        f=True
        cnt=0
        for y in range(len(beginning)):
            for x in range(len(beginning[0])):
                
                if (dy[y]+dx[x]) % 2==0:
                
                    if target[y][x]!=beginning[y][x]:
                        f=False
                        break
                        
                else:
                    if target[y][x]==beginning[y][x]:
                        f=False
                        break
            if not f:break
        if f:ans.append(sum(dx)+sum(dy))
    if len(ans)==0:return -1
    return min(ans)
                
                
ans_0=0
ans_1=0
def press(pos,k,arr):
    global ans_0, ans_1
    nx,ny=pos[0],pos[1]
    
    if k==1:
        return
    f=True
    c=arr[ny-1][nx-1]
    for y in range(k):
        for x in range(k):
            if arr[ny-1+y][nx-1+x]!=c:
                press([pos[0]+k//2,pos[1]],k//2,arr)
                press([pos[0],pos[1]+k//2],k//2,arr)
                press([pos[0]+k//2,pos[1]+k//2],k//2,arr)
                press([pos[0],pos[1]],k//2,arr)
                return
    if c==0:
        ans_0-=k*k-1
    else:
        ans_1-=k*k-1
        
        
    
        
    
    
def solution(arr):
    global ans_0 ,ans_1
    size=len(arr)
    for y in range(size):
        for x in range(size):
            if arr[y][x]==1:
                ans_1+=1
            else:
                ans_0+=1
            
    press([1,1],size,arr)
    answer = []
    return [ans_0,ans_1]
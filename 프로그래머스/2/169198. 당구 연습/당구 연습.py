def get(startX,startY,bx,by,x,y):
    temp=(abs(startX-x)**2+abs(startY-y)**2)**0.5
    temp2=(abs(bx-x)**2+abs(by-y)**2)**0.5
    return (temp+temp2)**2
def solution(m, n, startX, startY, balls):
    ans=[]
    max=10000000000
    for bx,by in balls:
        a=(startX+bx)**2+abs(startY-by)**2 #l
        b=((m-startX)+(m-bx))**2+abs(startY-by)**2 #r
        c=(startY+by)**2+abs(startX-bx)**2 #d
        d=((n-startY)+(n-by))**2+abs(startX-bx)**2 #u
        e=100000000
        
        if startY==by:
            if startX>bx:
                b=(m-startX+m-bx)**2 
                a=10000000
            elif startX<bx:
                a=(bx+startX)**2  
                b=100000000
        if startX==bx:
            if startY<by:
                c=(startY+by)**2
                d=10000000
            elif startY>by:
                d=(n+n-by-startY)**2
                c=100000000
        
            
        if by==startY*bx/a:
            if bx>startX:
                e=min(e,get(startX,startY,bx,by,0,0))
                
        if by==(n-startY)*(bx-startX)/(m-startX)+b:
            if bx<startX:
                e=min(e,get(startX,startY,bx,by,m,n))
            
        if by==(startY-n)*(bx-startX)/a +b:
            if bx>startX:
                e=min(e,get(startX,startY,bx,by,0,n))
                
        
            
        
        if by==startY*(bx-startX)/(startX-m)+b:
            if bx<startX:
                e=min(e,get(startX,startY,bx,by,m,0))
        
        ans.append(min(a,b,c,d,e))
    return ans
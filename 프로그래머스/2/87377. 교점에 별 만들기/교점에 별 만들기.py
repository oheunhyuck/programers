def is_parallel(A,B):
    if A[0]*B[1]==A[1]*B[0]:return True
    return False
def check(A,B,stars,xarr,yarr):


    a,b,e=A[0],A[1],A[2]
    c,d,f=B[0],B[1],B[2]
    
    x=(b*f-e*d)/(a*d-b*c)
    y=(e*c-a*f)/(a*d-b*c)
    
    if x%1==0 and y%1==0:
        stars.add((x,y))
        xarr.append(x)
        yarr.append(y)
    
def solution(line):
    answer = []
    stars=set()
    xarr=[]
    yarr=[]
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            if is_parallel(line[i],line[j]):continue
            check(line[i],line[j],stars,xarr,yarr)
    
    yup=int(max(yarr))
    ydown=int(min(yarr))
    xleft=int(min(xarr))
    xright=int(max(xarr))
    ans=[]
    answer=[]
    k=ydown
    for i in range(ydown,yup+1):
        s=""
        for j in range(xleft,xright+1):
            if (j,i) in stars:
                s+="*"
                
            else:
                s+="."
        ans.append(s)
    for i in range(len(ans)-1,-1,-1):
        answer.append(ans[i])
    return answer

    
    
    
    
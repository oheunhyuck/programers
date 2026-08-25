
    
    
def solution(storey):
    cnt=0
    storey=str(storey)
    for i in range(len(storey)-1,-1,-1):
        x=int(storey[i])
        if i==0:
            if x<=5:return cnt+x
            else:return cnt+(10-x)+1
        if x<5 or (x==5 and int(storey[i-1])<5 ):
            cnt+=x
            
        else:
            if i==0:return cnt+(10-x)+1
            cnt+=10-x
            temp=int(storey)
            n=len(storey)-i
            temp=temp+10**(n)
            storey=str(temp)
    return cnt
75
9

10
55
85

            
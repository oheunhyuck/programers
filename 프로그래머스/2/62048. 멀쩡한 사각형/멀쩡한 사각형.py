def solution(w,h):
    cnt=0
    ans=0
    l=0
    for i in range(1,w+1):
        temp=-1
        if (i*h) %w ==0:
            temp=(h*i//w)
            cnt+=(h*i//w)-l
            break
        else:
            temp=h*i//w
            cnt+=h*i//w+1-l
        l=temp
    ans+=(w//i)*cnt
    
    
    return (w*h)-ans
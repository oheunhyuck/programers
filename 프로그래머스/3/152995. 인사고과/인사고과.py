
def solution(scores):
    scores=[ scores[i]+[i] for i in range(len(scores))]
    scores.sort(key=lambda x:(-x[0],x[1]))
    temp=[]
    max_=0
    for a,b,i in scores:
        if b>=max_:
            temp.append([a+b,i])
            max_=max(b,max_)
            continue
        if i==0:return -1
        max_=max(b,max_)
    temp.sort(reverse=True)
    cnt=0
    l=-1
    t=0
    for s,i in temp:
        if s!=l:
            
            cnt+=1+t
            t=0
        else:
            t+=1
        if i==0:return cnt
        l=s
        
    
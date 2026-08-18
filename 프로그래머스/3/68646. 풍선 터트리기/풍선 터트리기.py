def solution(a):
    answer = 0
    d=[0]*len(a)
    min_v=1e9
    min_vv=1e9
    for i in range(len(a)):
        if a[i]<min_v:
            min_v=a[i]
        else:
            d[i]+=1
    for i in range(len(a)-1,-1,-1):
        if a[i]<min_vv:
            min_vv=a[i]
        else:
            if d[i]==1:
                answer+=1
            
    return len(a)-answer       
            
        
    
def solution(arr):
    arr=[[x,x] for x in arr]
    while True:
        f=True 
        mi=0
        m=arr[0][0]
        c=m
        for i,j in enumerate(arr):
            if j[0]!=c:
                f=False
            if j[0]<m:
                m=j[0]
                mi=i
        arr[mi][0]+=arr[mi][1]
        
        if f:  return c
        answer = 0
    return answer
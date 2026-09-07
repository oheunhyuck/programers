def solution(info, n, m):
    answer = 0
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    a_sum=0
    b_sum=0
    for A,B in info:
        if B+2==A:
            a.append([A,B])
        elif B+1==A:
            b.append([A,B])
        elif B==A:
            c.append([A,B])
        elif B-1==A:
            d.append([A,B])
        elif B-2==A:
            e.append([A,B])
    for i in a:
        if b_sum+i[1]<m:
            b_sum+=i[1]
        elif a_sum+i[0]<n:
            a_sum+=i[0]
        else:return -1
    for i in b:
        if b_sum+i[1]<m:
            b_sum+=i[1]
        elif a_sum+i[0]<n:
            a_sum+=i[0]
        else:return -1
    for i in c:
        if b_sum+i[1]<m:
            b_sum+=i[1]
        elif a_sum+i[0]<n:
            a_sum+=i[0]
        else:return -1
    for i in d:
        if b_sum+i[1]<m:
            b_sum+=i[1]
        elif a_sum+i[0]<n:
            a_sum+=i[0]
        else:return -1
    for i in e:
        if b_sum+i[1]<m:
            b_sum+=i[1]
        elif a_sum+i[0]<n:
            a_sum+=i[0]
        else:return -1
    return a_sum
        
        
        
        
        
    return answer
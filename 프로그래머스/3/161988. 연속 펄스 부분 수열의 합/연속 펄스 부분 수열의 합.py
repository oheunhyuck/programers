def get_max(arr):
    
    p=0
    temp=[]
    s=0
    while p<len(arr):
        if arr[p]<0:
            temp.append(s)
            if s+arr[p]<0:
                p+=1
                s=0
            else:
                s+=arr[p]
                p+=1
        else:
            s+=arr[p]
            p+=1
    temp.append(s)
    return max(temp)
            
    
def solution(sequence):
    answer = 0
    A=[]
    B=[]
    k=1
    for i in sequence:
        A.append(i*-k)
        B.append(i*k)
        k=-k
    return max(get_max(A),get_max(B))
    return answer
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    s=0
    for i,j in zip(A,B):
        s+=i*j
    
   

    return s
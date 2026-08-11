def solution(A, B):
    answer = -1
    A.sort()
    B.sort()
    ap=0
    bp=0
    cnt=0
    while bp<len(B):
        if B[bp]>A[ap]:
            cnt+=1
            bp+=1
            ap+=1
        else:
            bp+=1
    return cnt
        
    
    return answer
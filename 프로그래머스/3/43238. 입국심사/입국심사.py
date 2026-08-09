def is_possible(t,times,k,answer):
    s=0
    for i in times:
        s+=t // i
    
    
    if s>=k :
        answer.append(t)
        return True
    return False
def binary_search(s,e,times,k,answer):
    if s>e: return

    m=(s+e) // 2
    if is_possible(m,times,k,answer):
        binary_search(s,m-1,times,k,answer)
    else:
        binary_search(m+1,e,times,k,answer)
def solution(n, times):
    answer=[]
    binary_search(1,n*max(times),times,n,answer)
    answer.sort()
    return answer[0]
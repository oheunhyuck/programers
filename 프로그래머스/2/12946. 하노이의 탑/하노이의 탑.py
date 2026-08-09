def hanoi(s,e,n):
    if n==1:
        return [[s,e]]
    t=0
    for i in range(1,4):
        if i!=s and i!=e:
            t=i
            
    return hanoi(s,t,n-1)+[[s,e]]+hanoi(t,e,n-1)


def solution(n):
    answer = [[]]
    return hanoi(1,3,n)
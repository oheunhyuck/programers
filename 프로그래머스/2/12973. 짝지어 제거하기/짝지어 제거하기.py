def solution(k):
    s=[]
    for i in k:
        if s==[]:s.append(i)
        elif s[-1]==i:s.pop()
        else:s.append(i)
        
    if s==[]:return 1
    return 0
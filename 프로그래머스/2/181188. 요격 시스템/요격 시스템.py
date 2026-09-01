def solution(targets):
    answer = 0
    targets.sort()
    s=targets[0][0]
    e=targets[0][1]
    for i in range(1,len(targets)):
        ns,ne=targets[i][0],targets[i][1]
        if ns<e:
            s=ns
            e=min(e,ne)
        else:
            answer+=1
            

            s=ns
            e=ne
        
    return answer+1
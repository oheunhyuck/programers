def solution(skill, skill_trees):
    cnt=0
    p=0
    cur=skill[0]
    for i in skill_trees:
        cur=skill[0]
        p=0
        f=True
        for j in i:
            if j in skill:
                if j!=cur:
                    f=False
                    break
                else:
                    if p<len(skill)-1:
                        p+=1
                        cur=skill[p]
        if f:
            cnt+=1
        
    return cnt
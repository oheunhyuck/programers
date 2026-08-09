def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[0])
    l=routes[0]
    cnt=1
    for  i,j in enumerate(routes):
        if i==0:continue
        if j[0]<=l[1]:
            l=[j[0],min(l[1],j[1])]
        else:
            l=j
            cnt+=1
    return cnt
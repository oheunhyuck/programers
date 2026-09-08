from itertools import combinations
cnt=0
def check(idx,col,keys,relation):
    global cnt
    a=set()
    for k in keys:
        if len(set(k)-set(idx))==0:
            return
    for y in range(len(relation)):
        temp=[]
        for x in idx:
            temp.append(relation[y][x])
        a.add(tuple(temp))
    if len(a)==len(relation):
        cnt+=1
        keys.add(idx)
            
            
def solution(relation):
    answer = 0
    keys=set()
    index=[i for i in range(len(relation[0]))]
    col=[[] for i in range(len(relation[0]))]
    for y in  range(len(relation)):
        for x in range(len(relation[0])):
            col[x].append(relation[y][x])
    for c in range(1,len(relation[0])+1):
        for temp in combinations(index,c):
            check(temp,col,keys,relation)
    return cnt
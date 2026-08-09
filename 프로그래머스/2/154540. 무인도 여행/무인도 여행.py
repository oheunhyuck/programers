import sys
sys.setrecursionlimit(100000)
cnt=0
def dfs(v,i,j,maps):
    global cnt
    if v[i][j]==True or v[i][j]=="X":return
    v[i][j]=True
    cnt+=int(maps[i][j])
    if i-1>=0 and maps[i-1][j]!="X":
        dfs(v,i-1,j,maps)
    if j+1<len(maps[0]) and maps[i][j+1]!="X":
        
        dfs(v,i,j+1,maps)
    if i+1<len(maps) and maps[i+1][j]!="X":
        dfs(v,i+1,j,maps)
    if j-1>=0 and maps[i][j-1]!="X":
        dfs(v,i,j-1,maps)
    
    
    
def solution(maps):
    global cnt
    v=[[False]*(len(maps[0])) for _ in range(len(maps))]
    answer = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]!="X" and v[i][j]==False:
                cnt=0
                dfs(v,i,j,maps)
                answer.append(cnt)
                
    if answer==[]:return [-1]
    return sorted(answer)
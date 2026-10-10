
def get_short(r,p):
    
    temp=[]
    for i in range(len(r)-1):
        s=p[r[i]-1]
        e=p[r[i+1]-1]
        
        if s[0]<e[0]:

            temp+=[1]*(e[0]-s[0])
        elif s[0]>e[0]:
            temp+=[-1]*(s[0]-e[0])
        if s[1]<e[1]:

            temp+=[2]*(e[1]-s[1])
        elif s[1]>e[1]:
            temp+=[-2]*(s[1]-e[1]) 

    return temp
def solution(points, routes):
    answer = 0
    k=[]
    paths=[]
    cnt=0
    pos=[]
    for i in range(len(routes)):
        s=points[routes[i][0]-1]
        r=get_short(routes[i],points)
        pos.append(s[:])
        
        cnt=max(cnt,len(r))
        paths.append(r)
    ans=0
    v=[True]*(len(pos))
    for i in range(cnt+1):
        t=set()
        s=set()
        if i!=0:
            for j,r in enumerate(paths):
                if i>len(r):
                    v[j]=False
                    continue
                
                if r[i-1]==1:
                    pos[j][0]+=1
                    
                elif r[i-1]==-1:
                    pos[j][0]-=1
                elif r[i-1]==2:
                    pos[j][1]+=1
                elif r[i-1]==-2:
                    pos[j][1]-=1
                    
                
        c=0 
        
        for i,p in enumerate(pos):
                if v[i]:
                    if tuple(p) in t:
                        s.add(tuple(p))
                    else:
                        t.add(tuple(p))
                        
                    
        ans+=len(s)
        k.append(v)
            
            
        
        
    return ans
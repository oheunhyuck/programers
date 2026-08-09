def solution(n, s, a, b, fares):
    answer = 0
    INF=10 ** 100
    m=INF
    edge=[[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):edge[i][i]=0
    for k,i in enumerate(fares):
        d,e,f=i[0],i[1],i[2]
        edge[d][e]=f
        edge[e][d]=f
        
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if j==i or k==i:pass
                edge[j][k]=min(edge[j][k],edge[j][i]+edge[i][k])
                edge[k][j]=edge[j][k]
    for i in range(1,n+1):
        if i==a or i==b:pass
        temp=0
    
        if i==s:
            temp=edge[s][a]+edge[s][b]
        else:
            temp=edge[s][i]+edge[i][a]+edge[i][b]
        if temp<m:
            m=temp
    return m
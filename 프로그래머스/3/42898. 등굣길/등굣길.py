def solution(m, n, puddles):
    dp=[[0]*m for _ in range(n)]
    dp[0][0]=1
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:continue
            if [j+1,i+1]in puddles: continue
            s=0
            if i-1>=0:s+=dp[i-1][j]
            if j-1>=0:s+=dp[i][j-1]
            
                
            
            dp[i][j]=s

    

    return dp[n-1][m-1] % 1000000007
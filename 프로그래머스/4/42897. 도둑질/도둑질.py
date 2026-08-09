def solution(money):
    answer = 0
    m=len(money)
    l=0
    dp=[0]*m
    dp[0]=money[0]
    dp[1]=money[1]
    
    dp2=dp.copy()
    dp[2]=money[2]+money[0]
    dp[3]=dp[0]+money[3]
    dp2[2]=money[2]
    dp2[3]=dp2[1]+money[3]
    
    for i in range(4,m-1):
        dp[i]=max(dp[i-2],dp[i-3])+money[i]
        
    for i in range(4,m):
        dp2[i]=max(dp2[i-2],dp2[i-3])+money[i]
    
        
    return max(dp[m-2],dp[m-3],dp2[m-1],dp2[m-2])
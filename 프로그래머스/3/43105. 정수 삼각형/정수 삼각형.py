def solution(triangle):
    dp=[ [0]*len(triangle) for _ in range(len(triangle))]
    dp[0][0]=triangle[0][0]
    for i,j in enumerate(triangle):
       if i==0:continue
       for x,c in enumerate(j):
            if x==0:
                dp[i][x]=c+dp[i-1][x]
            elif x==len(j)-1:
                dp[i][x]=c+dp[i-1][x-1]
            else:    
            
                dp[i][x]=max(dp[i-1][x],dp[i-1][x-1])+c
       
    answer = 0
    
    return max(dp[len(triangle)-1])
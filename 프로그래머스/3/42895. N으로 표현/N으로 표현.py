def dcom(a,b,dp,i):
    
            dp[i].add(a+b)
            
            dp[i].add(a-b)
            dp[i].add(b-a)
            
            dp[i].add(a*b)
            
            if a!=0:dp[i].add(b//a)
            if b!=0:dp[i].add(a//b)
def com(A,B,dp,i):
    for a in A:
        for b in B:
            dcom(a,b,dp,i)
def solution(N, number):
    
    
    dp=[set() for _ in range(10)]
    dp[1].add(N)
    if N==number:return 1
    for i in range(2,9):
        for a in range(1,i//2+1):
            com(dp[a],dp[i-a],dp,i) 
            
        
        
        dp[i].add(int(str(N)*i))
        if number in dp[i]:return i
    return -1

                    
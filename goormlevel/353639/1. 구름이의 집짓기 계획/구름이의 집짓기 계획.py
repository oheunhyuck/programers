# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
n,k=map(int,input().split())

flowers=[]
for a in sys.stdin:
	a=int(a)
	flowers.append(a)
flowers=[0]+flowers
dp=[0]*(n+1)
for i in range(1,k+1):
	dp[i]=dp[i-1]+flowers[i]
for i in range(k+1,n+1):
		m=-1
		for j in range(1,k+2):
				if j==1:
					m=max(m,dp[i-j])
				else:
					s=0
					for h in range(j-1):
						s+=flowers[i-h]
					m=max(m,s+dp[i-j])
		dp[i]=m
print(dp[-1])
			

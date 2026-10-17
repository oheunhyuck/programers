import sys
input=sys.stdin.readline
n,m=map(int,input().split())
ground=[0]
v=set()
ground+=list(map(int,input().split()))
for i in range(1,m+1):
	
	s,e=map(int,input().split())
	for j in range(s,e+1):
		ground[j]+=1
		v.add(j)
	if i%3==0:
		for j in v:
			ground[j]-=1
		v=set()
for i in range(1,len(ground)):
	print(ground[i],end=" ")
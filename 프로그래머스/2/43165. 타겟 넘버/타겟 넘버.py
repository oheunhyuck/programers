cnt=0

def dfs(n,i,numbers,t):
    global cnt
    
    if i==len(numbers):
        if(n==t):cnt+=1
        return 

    dfs(n+numbers[i],i+1,numbers,t)
    dfs(n-numbers[i],i+1,numbers,t)
    
def solution(numbers, target):
    answer = 0
    dfs(0,0,numbers,target)
    return cnt
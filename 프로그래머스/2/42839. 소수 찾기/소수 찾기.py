from collections import Counter
cnt=0
s=set()
def is_prime(k):
    global s
    if(k==1 or k==0 or k in s):return False
    
    i=2
    
    while i*i<=k:
        if(k%i==0):return False
        i+=1
    s.add(k)
    return True

def check(k,c,n,numbers):
    global cnt
    if(is_prime(k)):cnt+=1
    
    for i in c:
        if(c[i]>=1):
            
            c[i]-=1
            check(k+i*n,c.copy(),n*10,numbers)
            c[i]+=1
            
    
    


def solution(numbers):
    numbers=list(map(int,numbers))
    c=Counter(numbers)
    
    for i in c:
        c[i]-=1
        check(i,c.copy(),10,numbers)
        c[i]+=1
        
    
    
    return cnt
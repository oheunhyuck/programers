def add_prime(prime,i,begin, end):
    p=i
    i=begin-(begin%i)
    
    while i<=end:
        if i-begin>=0:
            prime[i-begin].append(p)
        i+=p



def solution(begin, end):
    answer=[]
    v=set()
    prime=[[] for _ in range(end-begin+1)]
    for i in range(2,int((end**(0.5)))+1):
        
        add_prime(prime,i,begin,end)
    for i in range(begin,end+1):
        
        if i==1:
            answer.append(0)
            continue
        
        
        if len(prime[i-begin])==0:answer.append(1)
        
        else:
            res=1
            for j in prime[i-begin]:
                res=j
                if i//j<=10000000:
                    res=i//j
                    break
            answer.append(res)
        
    return answer
        
 
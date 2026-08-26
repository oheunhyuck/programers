from collections import Counter
def is_couple(a,b):
    if a==b or a*2==b*3 or a==b*2 or a*3==b*4 or b*2==a*3 or b==a*2 or b*3==a*4:return True
    return False
def solution(weights):
    cnt=0
    temp=[(2,3),(1,2),(3,4),(3,2),(2,1),(4,3)]
    
    v=set()
    counter=Counter(weights)
    for key in counter:
        v.add(key)
        n=counter[key]
        cnt+=n*(n-1)//2
        for a,b in temp:
            if (key*a) % b !=0:continue
            m=key*a//b
            if m in v:continue
            if m not in counter: continue
            m=counter[m]
            cnt+=n*m
    return cnt
            
            
        
        
    for i in range(len(weights)-1):
        for j in range(i+1,len(weights)):
            if weights[i]*2 <weights[j]:break
            if is_couple(weights[i],weights[j]):cnt+=1
            
    
    return cnt
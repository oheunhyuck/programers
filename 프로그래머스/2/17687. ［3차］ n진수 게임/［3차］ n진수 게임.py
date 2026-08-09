def change(num,n):
    dic={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    k=0
    s=[]
    while True:
        if num // (n**k)==0:
            k-=1
            break
        k+=1
    for i in range(k):
        
        if (num // (n**(k-i)))>=10:
            s.append(dic[(num // (n**(k-i)))])
        else:s.append(str((num // (n**(k-i)))))
            
        
        
        num-=(num // (n**(k-i)))*(n**(k-i))
    if num>=10:
        s.append(dic[num])
    else:
        s.append(str(num))
    
    
    return s
    
def solution(n, t, m, p):
    k=0
    l=0
    o=0
    answer=""
    while True:
        x=change(k,n)
        for j in x:
            l+=1
            if l==p or (l-p)%m==0:
                answer+=j
                o+=1
                if o==t:return answer
        k+=1
            
            
        
        

    return answer
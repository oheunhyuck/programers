import math
def get_(k):
    temp=[]
    for i in range(1,int(k**0.5)+1):
        if k%i==0:
            temp.append(i)
            temp.append(k//i)
    return temp
def get(array):
    
    b=set()
    k=math.gcd(*array)
    return get_(k)
    for i in array:
        temp=get_(i)
        for j in temp:
            b.add(j)
    return get_(k),b
   
    
    
def solution(arrayA, arrayB):
    answer = 0
    Amax,Bmax=0,0
    Alist=get(arrayA)
    Blist=get(arrayB)
    Alist.sort(reverse=True)
    Blist.sort(reverse=True)
    for a in Alist:
        f=True
        for b in arrayB:
            if b % a==0:
                f=False
                break
                
        if f:
            Amax=a
            break 
    for b in Blist:
        f=True
        for a in arrayA:
            if a % b==0:
                f=False
                break
                
        if f:
            Bmax=b
            break 
    return max(Amax,Bmax)
            
    for i in Blist:
        if i not in Aset:
            Bmax=i
            break
    return max(Amax,Bmax)
            
            
    
    return get(arrayA)
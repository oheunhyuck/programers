def solution(sequence, k):
    
    s=0
    e=0
    cur=0
    ans=[]

        
    while s<len(sequence)  :
        
        
        if cur<k:
            cur+=sequence[s]
            s+=1
            
            
            
        elif cur>k:
            cur-=sequence[e]
            e+=1
            
        if cur==k:
            ans.append((s-e,e,(s-1,e)))
            if s>=len(sequence):break
            cur+=sequence[s]
            s+=1   
    while e<len(sequence):
        cur-=sequence[e]
        e+=1
        if cur==k:
            ans.append((s-e,e,(s-1,e)))
            break
            
    ans.sort()       
    return [ans[0][2][1],ans[0][2][0]]
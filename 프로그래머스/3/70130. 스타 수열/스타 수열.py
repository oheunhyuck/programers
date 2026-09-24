from collections import Counter
def solution(a):
    answer = -1
    count=[]
    c=Counter(a)
    for k in c:
        count.append([c[k],k])#갯수 인뎃스
    count.sort(reverse=True)
    ans=0
    for cnt,index in count:
        if cnt==1:break
        #if len(a)-cnt<cnt:continue
        if ans>=cnt*2:break
        i=0
        cnt=0
        while i<len(a)-1:
            if  (index!=a[i] and index!=a[i+1]) or (index==a[i] and index==a[i+1]):
                i+=1
                continue
            if (index==a[i] or index==a[i+1]) and a[i]!=a[i+1]:
                cnt+=1
                i+=2
        ans=max(ans,cnt*2)
    return ans
        
            
            
            
        
    
        
    return Counter(a)
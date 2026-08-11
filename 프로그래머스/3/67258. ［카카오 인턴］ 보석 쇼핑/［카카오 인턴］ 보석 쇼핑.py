def solution(gems):
    answer = []
    counter={}
    for i,j in enumerate(gems):
        if j not in counter:
            counter[j]=0
    fp=0
    bp=0
    cnt=0
    ans=[]
    while fp<len(gems):
        if counter[gems[fp]]==0:cnt+=1
        
        counter[gems[fp]]+=1
        
            
        while counter[gems[bp]]>1:
                counter[gems[bp]]-=1
                bp+=1
                
                
        if cnt==len(counter):ans.append([bp+1,fp+1])  
        fp+=1
        
        
        
    ans.sort(key=lambda x: (x[1]-x[0],x[0]  ))
    return ans[0]
            
    
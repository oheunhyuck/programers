def solution(answers):
    answer = []
    k=[[1,0],[2,0],[3,0]]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        
        if answers[i]==a[i%5]:k[0][1]+=1
        if answers[i]==b[i%8]:k[1][1]+=1
        if answers[i]==c[i%10]:k[2][1]+=1
    k.sort(key= lambda x: x[1],reverse=True)
    
    for i in k:
       if(k[0][1]==i[1]):answer.append(i[0])
       else:break
       
    return answer
       
       
    answer.append()
    
        
        
        
        
        
        
    return answer
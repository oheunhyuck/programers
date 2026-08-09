def solution(want, number, discount):
    answer = 0
    dict_={}
    for i,j in zip(number,want):
        dict_[j]=i
    for i in range(len(discount)-9):
        temp=dict_.copy()
        f=True
        for j in range(i,i+10):
            if discount[j] not in temp or temp[discount[j]]==0:
                f=False
                break
            else:temp[discount[j]]-=1
        if f:answer+=1
        
        
                
            
        
    return answer
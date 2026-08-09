def solution(elements):
    answer = set()
    for i in range(len(elements)):
        s=elements[i]
        answer.add(s)
        for j in range(i+1,len(elements)):
            s+=elements[j]
            answer.add(s)
            
    for i in range(2,len(elements)):
        s=0
        for j in elements[i:]:
            s+=j
        for k in range(i-1):
            s+=elements[k]
            answer.add(s)
                
  
    return len(answer)
    
    return list(answer)
def solution(s):
    answer = ''
    a=s.split(" ")
    for p,k in enumerate(a):
        
        for i,j in enumerate(k):
            if j.isalpha():
                if i==0 :
                    answer+=j.upper()
                else:
                
                    answer+=j.lower()
            else:answer+=j
        if p!=len(a)-1:
            answer+=" "
        
        
        
        
    return answer
        
        
    return answer
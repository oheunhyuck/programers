def solution(phone_book):
    p=set(phone_book)
    for i in phone_book:
        s=""
        for c in i[:-1]:
            s+=c
            
            if s in p:
                return False
            
    answer = True
    
    return answer
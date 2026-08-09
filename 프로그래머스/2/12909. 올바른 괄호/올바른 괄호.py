def solution(ss):
    answer = True
    s=[]
    for i in ss:
        if(i=="("):
            s.append(1)
        else:
            if(len(s)==0):return False
            s.pop()
            
    if(len(s)==0):return True
    return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True
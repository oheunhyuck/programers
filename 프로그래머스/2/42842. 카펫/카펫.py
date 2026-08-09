def solution(brown, yellow):
    answer = []
    total=brown+yellow
    i=3
    while(i*i<=total):
        if(total % i)==0:
            y=(i-2)*(total/i-2)
            if(y==yellow):
                answer.append(total/i)
                answer.append(i)
        i+=1
        
        
    return answer
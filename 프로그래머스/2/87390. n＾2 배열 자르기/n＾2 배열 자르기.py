def get(col,i):
    if i<=col: return col
    return i

def solution(n, left, right):
    answer = []
    
    for i in range(left+1,right+2):
        if i%n==0:answer.append(get(i//n,n))
        else:
            answer.append(get(i//n+1,i-(i//n)*n))
    return answer
    
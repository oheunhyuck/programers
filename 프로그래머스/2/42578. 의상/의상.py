def solution(clothes):
    hash={}
    for i in clothes:
        if i[1] in hash:
            hash[i[1]]+=1
        else:
            hash[i[1]]=1
    answer=1
    for k in hash:
        answer*=(hash[k]+1)
    answer-=1
    return answer
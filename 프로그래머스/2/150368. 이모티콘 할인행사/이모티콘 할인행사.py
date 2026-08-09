from itertools import product
def solution(users, emotions):
    answer = []
    temp=[]
    for i in users:
        d=i[0]
        temp+=[d]*len(emotions)
    t=[i for i in range(1,41)]
    discount=list(product([10,20,30,40],repeat=len(emotions)))
    for d in discount:
        total_cost=0
        plus=0
        for user in users:
            cost=0
            for i in range(len(emotions)):
                if d[i]>=user[0]:cost+=emotions[i]//100*(100-d[i])
            if cost>=user[1]:
                plus+=1
            else:
                total_cost+=cost
        answer.append([plus,total_cost])
    answer.sort(reverse=True)               
    return answer[0]
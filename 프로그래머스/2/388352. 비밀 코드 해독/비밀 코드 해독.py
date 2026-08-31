from itertools import combinations
def solution(n, q, ans):
    answer = 0
    temp=[i+1 for i in range(n)]
    q=[set(i) for i in q]
    for password in combinations(temp,5):
        f=True
        for i,check in enumerate(q):
            cnt=0
            
            for p in password:
                if p in check:cnt+=1
            if cnt!=ans[i]:
                f=False
                break
        if f:
            answer+=1
            
    return answer
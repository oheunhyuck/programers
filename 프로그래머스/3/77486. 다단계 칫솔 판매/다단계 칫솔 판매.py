def give_money(money,up,income,cur):
    if money<10:
        income[cur]+=money
        return 
    
    if up[cur]=="-":
        income[cur]+=money-(money//10)
        return
    else:
        income[cur]+=money-(money//10)
        give_money(money//10,up,income,up[cur])
def solution(enroll, referral, seller, amount):
    answer = []
    income={}
    up={}
    
    ans=[]
    for e,u in zip(enroll,referral):
        income[e]=0
        up[e]=u
    
    
    
    for seller,amount in zip(seller,amount):
        money=amount*100
        give_money(money,up,income,seller)
        
    
    
    
    
    
    
    
    
    
    
    for e in enroll:
        ans.append(income[e])
        
    return ans
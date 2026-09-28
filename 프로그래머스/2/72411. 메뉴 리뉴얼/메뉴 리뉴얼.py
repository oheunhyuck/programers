from itertools import combinations
def solution(orders, course):
    ans=[]
    d=[0]*11
    a=[[] for _ in range(11)]
    dict_={}
    tt=set()
    for c in course:
        for o in orders:
            for k in combinations(o,c):
                if "".join(sorted(list(k))) in dict_:dict_["".join(sorted(list(k)))]+=1
                
                
                else:dict_["".join(sorted(list(k)))]=1
    for k in dict_:
        if dict_[k]>=2:
           
            if d[len(k)]<dict_[k]:
                d[len(k)]=dict_[k]
                a[len(k)]=[k]
                tt.add(len(k))
            elif d[len(k)]==dict_[k]:
                tt.add(len(k))
                a[len(k)].append(k)
    for m in tt:
        for i in a[m]:
            ans.append(i)
    
    ans.sort()
    return ans
                
                
            
    
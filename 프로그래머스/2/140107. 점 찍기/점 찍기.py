def get_h(x,d):
    return int((d**2 - x**2)**0.5)
def solution(k, d):
    d
    ak=[]
    a=0
    while a*k<=d:
        ak.append(a*k)
        a+=1
    bk=[]
    b=0
    while b*k<=d:
        bk.append(b*k)
        b+=1
        
    cnt=0
    for x in ak:
        h=get_h(x,d)
        cnt+= h//k +1
    return cnt
        
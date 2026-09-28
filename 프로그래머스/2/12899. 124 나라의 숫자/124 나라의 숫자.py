
def solution(n):
    i=0
    temp=[]
    
    while n // (3**i)>0:
        n-=(3**i)
        i+=1
        temp.append(1)
    i-=1
    p=len(temp)-1
    while n>0:
        temp[p]+=n//(3**i)
        n %= (3**i)
        p-=1
        i-=1
    for i in range(len(temp)):
        if temp[i]==3:
            temp[i]='4'
        else:
            temp[i]=str(temp[i])
    temp.reverse()
    return "".join(temp)
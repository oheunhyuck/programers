import sys
sys.setrecursionlimit(10**6)
ans=0
def binary_search(s,e,topping,b,c):
    if s>e:return
    m=(s+e)//2
    k=cut(topping,m,b,c)
    
    if k==1:binary_search(s,m-1,topping,b,c)
    elif k==2:binary_search(m+1,e,topping,b,c)
    elif k==3:
        binary_search(s,m-1,topping,b,c)
        binary_search(m+1,e,topping,b,c)
        
    
def cut(topping,cut,b,c):
    global ans
    
    x,y=b[cut],c[cut+1]
    if x>y:return 1
    elif x<y:return 2
    else:
        ans+=1
        return 3
        

    
def solution(topping):
    a=set()
    b=[0]*(len(topping))
    c=[0]*(len(topping))
    for i in range(len(topping)):
        if i==0:
            a.add(topping[i])
            b[i]=1
            continue
            
            
        if topping[i] in a:
            b[i]=b[i-1]
        else:
            a.add(topping[i])
            b[i]=b[i-1]+1
    a=set()
    for i in range(len(topping)-1,-1,-1):
        if i==len(topping)-1:
            a.add(topping[i])
            c[i]=1
            continue
            
            
        if topping[i] in a:
            c[i]=c[i+1]
        else:
            a.add(topping[i])
            c[i]=c[i+1]+1
    binary_search(0,len(topping)-1,topping,b,c)
    return ans
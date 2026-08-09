def solution(expression):
    answer = []
    
# + * -
    x=expression.split("-")
    ttemp=[]
    for i in x:
        y=i.split("*")
        temp=[]
    
        for j in y:
            z=j.split("+")
            t=0
            for k in z:
                t+=int(k)
            temp.append(t)
    
        pp=1
        for p in temp:
            pp*=p
        ttemp.append(pp)
    s=ttemp[0]*2
    for n in ttemp:
        s-=n
    answer.append (abs(s))

        

# + - *
    x=expression.split("*")
    ttemp=[]
    for i in x:
        y=i.split("-")
        temp=[]
    
        for j in y:
            z=j.split("+")
            t=0
            for k in z:
                t+=int(k)
            temp.append(t)
    
        pp=temp[0]*2
        for p in temp:
            pp-=p
        ttemp.append(pp)
    s=1
    for n in ttemp:
        s*=n
    answer.append (abs(s))
# * + -
    x=expression.split("-")
    ttemp=[]
    for i in x:
        y=i.split("+")
        temp=[]
    
        for j in y:
            z=j.split("*")
            t=1
            for k in z:
                t*=int(k)
            temp.append(t)
    
        pp=0
        for p in temp:
            pp+=p
        ttemp.append(pp)
    s=ttemp[0]*2
    for n in ttemp:
        s-=n
    answer.append (abs(s))
# * - +
    x=expression.split("+")
    ttemp=[]
    for i in x:
        y=i.split("-")
        temp=[]
    
        for j in y:
            z=j.split("*")
            t=1
            for k in z:
                t*=int(k)
            temp.append(t)
    
        pp=temp[0]*2
        for p in temp:
            pp-=p
        ttemp.append(pp)
    s=0
    for n in ttemp:
        s+=n
    answer.append (abs(s))
# - + *
    x=expression.split("*")
    ttemp=[]
    for i in x:
        y=i.split("+")
        temp=[]
    
        for j in y:
            z=j.split("-")
            t=int(z[0])*2
            for k in z:
                t-=int(k)
            temp.append(t)
    
        pp=0
        for p in temp:
            pp+=p
        ttemp.append(pp)
    s=1
    for n in ttemp:
        s*=n
    answer.append (abs(s))
# - * +
    x=expression.split("+")
    ttemp=[]
    for i in x:
        y=i.split("*")
        temp=[]
    
        for j in y:
            z=j.split("-")
            t=int(z[0])*2
            for k in z:
                t-=int(k)
            temp.append(t)
    
        pp=1
        for p in temp:
            pp*=p
        ttemp.append(pp)
    s=0
    for n in ttemp:
        s+=n
    answer.append (abs(s))
    return max(answer)
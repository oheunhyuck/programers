def is_correct(a,b,p):
    s=[]
    
    for k in range(a,b+1):
        if p[k]=="(":s.append(1)
        else:
            if len(s)==0:return False
            s.pop()
    return True
def is_balance(a,b,p):
    
    
    if a>b:return True
    cnt=0
    cnt_=0
    for k in range(a,b+1):
        if p[k]=="(":cnt+=1
        else:cnt_+=1
    if cnt==cnt_:return True

    return False
        
def process(p):
    if p=="":return ""
    for i in range(1,len(p),2):
        f=False
        if is_balance(0,i,p)==False or is_balance(i+1,len(p)-1,p)==False:
            continue
            
        for j in range(1,i-1,2):
            if is_balance(0,j,p)==True and is_balance(j+1,i,p)==True:
                
                f=True
                break
        if f==True:continue
        if is_correct(0,i,p)==True:
            return p[:i+1]+process(p[i+1:])
        else:
            temp="("
            temp+=process(p[i+1:])
            temp+=")"
            for k in range(i+1):
                if k==0 or k==i:continue
                if p[k]=="(":temp+=")"
                else:temp+="("
            return temp
    
def solution(p):
    return process(p)
    
                
        
            
            
        
        
    answer = ''
    return answer
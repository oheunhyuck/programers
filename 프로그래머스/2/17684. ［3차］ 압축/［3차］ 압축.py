global idx

def find(msg,dict_):
    global idx
    s=msg[idx]
    
    f=True
    while s in dict_:
        idx+=1
        if idx>=len(msg):
            f=False
            break
        s+=msg[idx]
    if f:
        
        s=s[:len(s)-1]
    return s
    
        
    
        
    
def solution(msg):
    global idx
    answer = []
    l=27
    dict_={}
    idx=0
    ans=[]
    for i in range(1,27):
        dict_[chr(64+i)]=i
    while True:
        w=find(msg,dict_)
        ans.append(dict_[w])
        if len(msg)<=idx:break
        dict_[w+msg[idx]]=l
        l+=1
    
    return ans
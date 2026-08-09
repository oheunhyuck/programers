from collections import Counter
def solution(str1, str2):
    A=[]
    B=[] 
    for i in range(0,len(str1)-1):
        a,b=ord(str1[i]),ord(str1[i+1])
       
        if ((65<=a and a<=90) or (97<=a and a<=122)) and ((65<=b and b<=90) or (97<=b and b<=122)):
            A.append(chr(a).upper()+chr(b).upper())
            
    for i in range(0,len(str2)-1):
        a,b=ord(str2[i]),ord(str2[i+1])
       
        if ((65<=a and a<=90) or (97<=a and a<=122)) and ((65<=b and b<=90) or (97<=b and b<=122)):
            B.append(chr(a).upper()+chr(b).upper())
    if len(A)==0 and len(B)==0:return 65536
    C=Counter(A)
    D=Counter(B)
    temp= (C&D)
    temp_= (C|D)
    cnt=0
    cnt_=0
    for i in temp:
        cnt+=temp[i]
    for i in temp_:
        cnt_+=temp_[i]
        
    return int(cnt/cnt_*65536)
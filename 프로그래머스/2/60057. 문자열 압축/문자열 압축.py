def solution(s):
    ans=10000
    if len(s)==1:return 1
    for size in range(1,len(s)//2+1):
        cnt=0
        i=size
        cnt+=len(s)%size
        rep=1
        while i<(len(s)-(len(s)%size))-size+1:
            j=0
            f=True
            while j<size:
                if s[i+j]!=s[i-size+j]:
                    f=False
                    break
                j+=1
            if f:
                rep+=1
            else:
                if rep==1:cnt+=size
                else:
                    cnt+=len(str(rep))+size
                rep=1
            i+=size
        if rep==1:cnt+=size
        else:
            cnt+=len(str(rep))+size
        ans=min(ans,cnt)
    return ans
def solution(name):
    cnt=0
    for n in name:
        
        if ord(n)<=77:
            cnt+=ord(n)-65
        else:
            cnt+=90-ord(n)+1
    
    length=len(name)
    move=length-1
    
    for i in range(length):
        nxt=i+1
        while nxt<length and name[nxt]=="A":
            nxt+=1
        move=min(move,i*2+length-nxt,i+2*(length-nxt))
            
    return cnt+move
def c(a):
    hour,minites=map(int,a.split(":"))
    return hour*60+minites
    
def solution(m, musicinfos):
    ans=[]
    t=""
    i=0
    while i<len(m):
        if i<len(m)-1 and m[i+1]=='#':
            t+=m[i].lower()+'#'
            i+=2
        else:
            t+=m[i]
            i+=1

            
    for music in musicinfos:
        music=music.split(",")
        
        temp=c(music[1])-c(music[0])
        p=0
        s=""
        cnt=0
        while cnt<temp:
            if p<len(music[3])-1 and music[3][p+1]=='#':
                s+=music[3][p].lower()+"#"
                p+=2
                
            else:
                s+=music[3][p]
                p+=1
            if p==len(music[3]):p=0
            
            cnt+=1
            
            
        ans.append((temp,music[2],s))
    ans.sort(reverse=True,key=lambda x:x[0])

    for a in ans:
        if t in a[2]:return a[1]
    return "(None)"
    
                
            
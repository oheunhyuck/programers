class Node:
    def __init__(self,data):
        self.up=None
        self.down=None
        self.data=data

      
def solution(n, k, cmd):
    l=None
    p=None
    deleted=[]
    for i in range(n-1):
        
        if i==0:
            x,y=Node(i),Node(i+1)
            x.down=y
            y.up=x
            l=y
        else:
            t=Node(i+1)
            l.down=t
            t.up=l
            l=t
        if i==k:p=l.up
    if k==n-1:p=l
    for cmd in cmd:
        if cmd[0]=="U":
            x=cmd.split(" ")
            for _ in range(int(x[1])):
                p=p.up
            
        if cmd[0]=="D":
            x=cmd.split(" ")
            for _ in range(int(x[1])):
                p=p.down
        if cmd[0]=="C":
            x,y=p.up,p.down
            if x==None:
                y.up=None
                p.down=None
                deleted.append([0,p,y])
                p=y
            elif y==None:
                x.down=None
                p.up=None
                deleted.append([1,p,x])
                p=x
                
            else:
                x.down=y
                y.up=x
                p.up=None
                p.down=None
                deleted.append([2,p,x,y])
                p=y
            
        if cmd[0]=="Z":
            k=deleted.pop()
            if k[0]==0:
                t,y=k[1],k[2]
                t.down=y
                y.up=t
            if k[0]==1:
                t,x=k[1],k[2]
                t.up=x
                x.down=t
            if k[0]==2:
                t,x,y=k[1],k[2],k[3]
                t.down=y
                y.up=t
                t.up=x
                x.down=t
    t=0
    answer=""
    while p.up!=None:
        p=p.up
        
    while p.down!=None:
        while p.data>t:
            answer+="X"
            t+=1
        answer+="O"
        t+=1
        p=p.down
    while p.data>t:
            answer+="X"
            t+=1
    answer+="O"
    t+=1
    while t<=n-1:
        answer+="X"
        t+=1
    return answer
        

        
        
            
            
        
        
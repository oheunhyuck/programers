class Node:
    def __init__(self,id):
        self.up=[]
        self.down=[]
        self.id=id
    def get_up(self,v):
        v.add(self.id)
        if self.up==[]:return 1
        cnt=1
        for u in self.up:
            if u.id not in v:
                cnt+=u.get_up(v)
        return cnt
    def get_down(self,v):
        v.add(self.id)
        if self.down==[]:return 1
        cnt=1
        for u in self.down:
            if u.id not in v:               
                cnt+=u.get_down(v)
        return cnt
    
            
def solution(n, results):
    ans = 0
    Nodes=[Node(i) for i in range(n+1) ]
    for a,b in results:
        Nodes[a].down.append(Nodes[b])
        Nodes[b].up.append(Nodes[a])
    for i in range(1,n+1):
        if n-1==Nodes[i].get_up(set())+Nodes[i].get_down(set())-2:
            ans+=1
    return ans
import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self,x,y,id):
        self.x=x
        self.y=y
        self.id=id
        self.left=None
        self.right=None
    def addNode(self,n):
        if self.x>n.x:
            if self.left==None:
                self.left=n
            else:
                self.left.addNode(n)
        else:
            if self.right==None:
                self.right=n
            else:
                self.right.addNode(n)
def pre(n,a):
    a.append(n.id)
    if n.left!=None:
        pre(n.left,a)
    if n.right!=None:
        pre(n.right,a)
    
def post(n,b):
    if n.left!=None:
        post(n.left,b)
    if n.right!=None:
        post(n.right,b)
    b.append(n.id)
def solution(nodeinfo):
    nodeinfo=[nodeinfo[i]+[i+1] for i in range(len(nodeinfo)) ]
    nodeinfo.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    nodelist=[]
    for i in nodeinfo:
        nodelist.append(Node(i[0],i[1],i[2]))
    for i in range(1,len(nodelist)):
        nodelist[0].addNode(nodelist[i])
    a,b=[],[]
    pre(nodelist[0],a)
    post(nodelist[0],b)
    return [a,b] 


        
    answer = [[]]
    return nodeinfo
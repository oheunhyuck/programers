def union(parent,a,b):
    pa,pb=find(parent,a),find(parent,b)
    if pa==pb:return False
    parent[pa]=pb
    return True

def find(parent,k):
    
    while parent[k]!=k:
        k=parent[k]
    return k

def solution(n, costs):
    answer = 0
    s=0
    v=0
    parent=[i for i in range(n)] 
    costs.sort(key=lambda x: x[2])
    for a,b,c in costs:
        
        if union(parent,a,b):
            s+=c
            v+=1
        if v==n-1:return s
            
    return answer
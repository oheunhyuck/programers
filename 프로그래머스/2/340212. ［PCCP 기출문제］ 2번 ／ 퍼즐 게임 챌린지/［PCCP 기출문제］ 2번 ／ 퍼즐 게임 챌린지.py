ans=0
def binary_search(s,e,diff,times,limit,time_prev):
    global ans
    if s>e:return
    mid=(s+e)//2
    if is_possible(mid,diff,times,limit,time_prev):
        ans=mid
        binary_search(s,mid-1,diff,times,limit,time_prev)
    else:
        binary_search(mid+1,e,diff,times,limit,time_prev)
    
    
def is_possible(level,diff,times,limit,time_prev):
    used_time=0
    for cur in range(len(diff)):
        
        if diff[cur]<=level:
            used_time+=times[cur]
        else:
            if cur==0:
                used_time=(diff[cur]-level+1)*times[cur]
            else: 
                used_time+=(diff[cur]-level+1)*times[cur]+(times[cur-1])*(diff[cur]-level)
        if used_time>limit:return False
    return True
def solution(diffs, times, limit):
    answer = 0
    time_prev=[0]*len(diffs)
    for i in range(len(time_prev)):
        if i==0:
            time_prev[i]=times[i]
            continue
        
        time_prev[i]=time_prev[i-1]+times[i]
    
    
    binary_search(1,max(diffs),diffs,times,limit,time_prev)
    return ans
def go(i,cost,hint,used,ans,have_hint):
    f=False

    if i==len(cost)-1: 
        if len(cost)-1<have_hint[i]:
            have_hint[i]=len(cost)-1
        ans.append(used+cost[i][have_hint[i]]) 
        return

    go(i+1,cost,hint,used+cost[i][have_hint[i]],ans,have_hint)

    temp=have_hint.copy()
    for k in range(1,len(hint[i])):
        if have_hint[hint[i][k]-1]<len(cost)-1:
            have_hint[hint[i][k]-1]+=1

    go(i+1,cost,hint,used+cost[i][temp[i]]+hint[i][0],ans,have_hint)
    have_hint.update(temp)


def solution(cost, hint):
    ans=[]
    have_hint={i:0 for i in range(len(cost))}
    go(0,cost,hint,0,ans,have_hint)
    return min(ans)
def is_pal(p,arr):
    
    for i in range(1,min(p+1,len(arr)-p )):
        if arr[p+i]!=arr[p-i]:return (i-1)*2+1
    return min(p,len(arr)-p-1)*2+1

def is_pal_(p,arr):
    if p==0:
        if arr[0]==arr[1]:return 2
        return 0
    if p==len(arr)-2:
        if arr[len(arr)-2]==arr[len(arr)-2+1]:return 2
        return 0
    
    for i in range(0,min( p+1,len(arr)-p-1)):
        if arr[p-i]!=arr[p+1+i]:return i*2
    
    return (min(p,len(arr)-p-2)+1)*2


def solution(s):
    answer = 0
    if len(s)==1:return 1
    if len(s)==2:
        if s[0]==s[1]:return 2
        return 1
    for p in range(1,len(s)-1):
        answer=max(answer,is_pal(p,s))
    for p in range(0,len(s)-1):
        answer=max(answer,is_pal_(p,s))

    

    return answer
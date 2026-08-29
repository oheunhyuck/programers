from math import factorial
def get(arr,a):
    cnt=0
    for i in range(len(arr)):
        if arr[i]!=0:
            cnt+=1
            if cnt==a:
                temp=arr[i]
                arr[i]=0
                return temp
    return -1
def solution(n, k):
    answer = []
    arr=[i+1 for  i in range(n)]
    for i in range(n,0,-1):
        temp=factorial(i-1)
        if k%temp==0:
            a=k//temp
        else:
            a=(k // temp)+1
        k-=(a-1) *temp
        a=get(arr,a)
        answer.append(a)
        
    return answer
   





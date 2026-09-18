def is_prime(n):
    if n==1:return False
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:return False
    return True
def change(base,n):
    arr=[]
    while n>0:
        arr.append(str(n%base))
        n=n//base
    arr.reverse()
    return arr
    
    
    
def solution(n, k):
    answer = -1
    arr=change(k,n)
    cnt=0
    i=0
    while i<len(arr):
        s=""
        if arr[i]=="0":
            i+=1
            continue
        while i<len(arr)and arr[i]!="0":
            s+=arr[i]
            i+=1
        if is_prime(int(s)):
            cnt+=1
    return cnt
    
                   
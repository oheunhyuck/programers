def solution(n, l, r):
    ans=0
    A="11011"
    for j in range(l-1,r):
        trace=[]
        temp=j
        for i in range(n):
            trace.append(temp%5)
            temp=temp//5
        trace.reverse()
        for d in trace:
            if A[d]=='0':
                break
        else:
            ans+=1
    return ans
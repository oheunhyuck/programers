def solution(n, s):
    if n>s:return [-1]
    if s % n==0: 
        return [s//n]*n
    else:
        t=s%n
        k= [s//n]*n
        for j in range(t):
            k[j]+=1
        return sorted(k)
            
            

    answer = []


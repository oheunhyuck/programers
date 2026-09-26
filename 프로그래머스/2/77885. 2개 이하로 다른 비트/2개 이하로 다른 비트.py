def solution(numbers):
    ans=[]
    
    for number in numbers:
        num=['0']+list(bin(number)[2:])
        p=len(num)-1
        while 0<=p:
            if num[p]=='0':
                num[p]='1'
                break
                
            p-=1
        p+=1
        while p<len(num):
            if num[p]=='1':
                num[p]='0'
                break
            p+=1
        
        ans.append(int("".join(num),2))
            
    return ans
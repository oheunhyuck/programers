def solution(s):
    answer = []
    temp=[set() for _ in range(500)]
    p=0
    i=2
    cnt=0
    while i<len(s):
        cnt+=1
        while s[i]!="}":
            if s[i]==",":
                i+=1
                continue
            k=""
            while s[i].isdigit():
                k+=s[i]
                i+=1
            temp[p].add(int(k))
            
                
            
        p+=1
        i+=3
    arr=[set() for _ in range(cnt)]
    for i in range(cnt):
        arr[i]=temp[i]
    arr.sort(key=lambda x:len(x))
    answer=[]
    l=set()
    for x in arr:
        answer.append(int((x-l).pop()))
        l=x
    return answer
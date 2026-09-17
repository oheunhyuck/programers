def solution(data, col, row_begin, row_end):
    answer = 0
    sn=[]
    ans=0
    data.sort(key=lambda x:(x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        temp=data[i-1]
        s=0
        for d in temp:
            s+= d%i
        ans=ans ^ s
    return ans
    
            
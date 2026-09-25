def solution(files):
    ans=[]
    for file in files:
        p=0
        head=""
        num=""
        while p<len(file):
            if file[p].isdigit():
                while p<len(file) and file[p].isdigit():
                    num+=file[p]
                    p+=1
                break
                    
            else:
                head+=file[p].lower()
                p+=1
        ans.append([file,head,int(num)])
    ans.sort(key=lambda x:(x[1],x[2]))
    answer=[]
    for a  in ans:
        answer.append(a[0])
    #return ans
    
    return answer
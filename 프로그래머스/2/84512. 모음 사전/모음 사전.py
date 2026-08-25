import sys
sys.setrecursionlimit(10**6)
def bruteforce(word,n,dict_,temp):
    dict_[word]=n
    if word=="UUUUU":   
        return
    if len(word)!=5:
        bruteforce(word+"A",n+1,dict_,temp)
    else:
        if word[4]=="U":
            word=word[:4]
            for i in range(3,-1,-1):
                if word[i]=="U":
                    word=word[:i]
                    
                    
                else:
                    word=word[:i]+temp[word[i]]
                    break
                    
        else:
            word=word[:4]+temp[word[4]]
        bruteforce(word,n+1,dict_,temp)
                
                
                
        
        
        
def solution(word):
    answer = 0
    temp={"A":"E","E":"I","I":"O","O":"U","U":"A"}
    dict_={}
    bruteforce("A",1,dict_,temp)
    return dict_[word]
from functools import cmp_to_key
def compare(a,b):
    if str(a)+str(b)>str(b)+str(a):
        return -1
    return 1
    
def solution(numbers):
    
    numbers.sort(key=cmp_to_key(compare))
    answer="".join(map(str, numbers))
    if(answer[0]=="0"):answer="0"
    
    return answer
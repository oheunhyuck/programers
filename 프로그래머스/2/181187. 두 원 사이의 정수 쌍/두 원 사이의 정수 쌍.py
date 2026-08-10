
def solution(r1, r2):
    cnt=0
    s=0
    for x in range(1,r2+1):
        if x>r1:
            s+=int(((r2**2)-(x**2))  **0.5)+1
            
        else:
            if (((r1**2)-(x**2)) **0.5) % 1==0:
                s+=int(((r2**2)-(x**2))  **0.5)- (((r1**2)-(x**2))  **0.5) +1
            else:
                 s+=int(((r2**2)-(x**2))  **0.5)- int(((r1**2)-(x**2))  **0.5)
                
            
    return s*4
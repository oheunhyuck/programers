def solution(n):
    ans = 0
    i=n
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    while i!=0:
        if i % 2==0:
            i= i//2
        else:
            i-=1
            ans+=1

    return ans
     
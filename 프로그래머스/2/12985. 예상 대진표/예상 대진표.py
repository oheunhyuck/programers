def get_win_num(a):
    if a%2==0:
        return a//2
    return (a//2)+1
def is_fight(a,b):
    temp=a
    a=min(a,b)
    b=max(temp,b)
    if a+1!=b:return False
    if a%2==0:return False
    return True
def solution(n,a,b):
    cnt=1
    while True:
        if not is_fight(a,b):
            a=get_win_num(a)
            b=get_win_num(b)
            cnt+=1
        else:return cnt

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
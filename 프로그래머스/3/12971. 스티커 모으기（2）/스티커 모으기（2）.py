def solution(sticker):
    answer = 0
    if len(sticker)<3:
        return max(sticker)
    dp=[0]*len(sticker)
    dp[0]=sticker[0]
    dp[1]=0
    dp[2]=sticker[0]+sticker[2]
    for i in range(3,len(sticker)-1):
        dp[i]=max(dp[i-2],dp[i-3])+sticker[i]
    dp_=[0]*len(sticker)
    dp_[0]=0
    dp_[1]=sticker[1]
    dp_[2]=sticker[2]
    for i in range(3,len(sticker)):
        dp_[i]=max(dp_[i-2],dp_[i-3])+sticker[i]
    
    return max(dp[-2],dp[-3],dp_[-1],dp_[-2])
    
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
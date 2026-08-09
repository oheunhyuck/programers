def solution(n, words):
    answer = []
    used_words=set()
    last_word=words[0][0]
    turn=0
    for i in words:
        turn+=1
        
        if i in used_words or last_word[-1]!=i[0] or len(i)==1:
            if turn%n==0:
                return [n,turn // n ]
            return [turn%n,turn // n +1]
            break
        
        last_word=i
        used_words.add(i)
    return [0,0]
        
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
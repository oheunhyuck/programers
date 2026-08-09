def solution(s):
    answer = []
    z_cnt=0
    b_cnt=0
    while s!="1":
        b_cnt+=1
        temp=0
        for k in s:
            if k=="1":temp+=1
        z_cnt+=len(s)-temp
        s=str(bin(temp)[2:])
    return [b_cnt,z_cnt]
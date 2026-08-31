def difftime(in_time,out_time):
    c,d=map(int,in_time.split(":"))
    a,b=map(int,out_time.split(":"))
    return (a-c)*60+(b-d)
    
    
def cost(time,fees):
    s=0
    s+=fees[1]
    if time<=fees[0]:return fees[1]
    time-=fees[0]
    if (time) % fees[2]==0:
        
        s+=((time) //fees[2])*fees[3]
    else:
        s+=((time) //fees[2] +1)*fees[3]
    return  s
def solution(fees, records):
    answer = []
    dict_={}
    time_dict={}
    for data in records:
        time,id_,state=data.split()
        if state=="IN":
            dict_[id_]=time
            
        if state=="OUT":
            
            in_time=dict_[id_]
            del dict_[id_]
            out_time=time
            if id_ in time_dict:
                time_dict[id_]+=difftime(in_time,out_time)
            else:
                time_dict[id_]=difftime(in_time,out_time)
                
                
    for id_ in dict_:
        in_time=dict_[id_]
        out_time="23:59"
        if id_ in time_dict:
                time_dict[id_]+=difftime(in_time,out_time)
        else:
                time_dict[id_]=difftime(in_time,out_time)
                
    ans=[]
    for key in time_dict:
        
        ans.append([key,cost(time_dict[key],fees)])
    ans.sort(key=lambda x:x[0])
    a=[ans[i][1] for i in range(len(ans))]
    return a
    
        
    return answer
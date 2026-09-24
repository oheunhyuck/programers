def c(s):
    hour,minutes=map(int,s.split(":"))
    return hour*60+minutes
    
    
def solution(plans):
    fin=[]
    
    answer = []
    plans.sort(key=lambda x:x[1])
    waiting=[]
    last_start_time=-1
    last_take_time=-1
    last_subject="-1"
    
    for i in range(len(plans)):
        plans[i][1]=c(plans[i][1])
        plans[i][2]=int(plans[i][2])  
        
    for subject,start_time,take_time in plans:
        if last_subject=='-1':
            last_start_time=start_time
            last_take_time=take_time
            last_subject=subject
            continue
        
            
        if start_time-last_start_time==last_take_time:
            fin.append(last_subject)
            
            
            
        elif start_time-last_start_time>last_take_time:
            fin.append(last_subject)
            have_time=(start_time-last_start_time)-last_take_time
            while True and waiting:
                waiting_subject,waiting_take_time=waiting.pop()
                if have_time==waiting_take_time:
                    fin.append(waiting_subject)
                    break
                elif have_time>waiting_take_time:
                    fin.append(waiting_subject)
                    have_time-=waiting_take_time
                else:
                    waiting.append([waiting_subject,waiting_take_time-have_time])
                    
                    break
                
            
            
        else:
            waiting.append([last_subject,last_take_time-(start_time-last_start_time)])
            
        
        
        last_start_time=start_time
        last_take_time=take_time
        last_subject=subject
    waiting.append([last_subject,last_take_time])
    while waiting:
        fin.append(waiting.pop()[0])
    return fin
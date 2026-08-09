def solution(caps, n, deliveries, pickups):
    answer = -1
    d_cnt=0
    g_cnt=0
    move=0
    dm=n-1
    gm=n-1
    for i,j in zip(deliveries,pickups):
        d_cnt+=i
        g_cnt+=j
    
    while d_cnt>0 or g_cnt>0:
        if d_cnt>=caps:
            have=caps
        else:have=d_cnt
        f=-1
        for i in range(dm,-1,-1):
            if deliveries[i]>0:
                if f==-1:f=i
                if deliveries[i]<=have:
                    have-=deliveries[i]
                    d_cnt-=deliveries[i]
                    deliveries[i]=0
                    dm=i-1
                    
                    
                else:
                    deliveries[i]-=have
                    d_cnt-=have
                    have=0
                    
                    
                    
                if have==0:break
        for i in range(gm,-1,-1):
            if pickups[i]>0:
                if i>f:f=i
                if pickups[i]<=caps-have:
                    
                    have+=pickups[i]
                    g_cnt-=pickups[i]
                    pickups[i]=0
                    gm=i-1
                    
                else:
                    
                    pickups[i]-=caps-have
                    g_cnt-=caps-have
                    have=caps
                if have==caps:break
        move+=(f+1)*2
                    
    return move
            
            
        
        
  
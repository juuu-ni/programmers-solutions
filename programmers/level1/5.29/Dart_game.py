def solution(dartResult):
    scores = [] 

    for i in dartResult:
        if i.isdigit():
            if scores and scores[-1]==1 and i=="0":
                scores.pop()
                scores.append(10)
            else:
                scores.append(int(i))
                
        elif i=="S":
            scores[-1]=scores[-1]**1
        elif i=="D":
            scores[-1]=scores[-1]**2
        elif i=="T":
            scores[-1]=scores[-1]**3
            
        elif i=="*":
            scores[-1]=scores[-1]*2
            if len(scores)>=2:
                scores[-2] = scores[-2]*2
                
        elif i=="#":
            scores[-1] = scores[-1] * -1
    
    return sum(scores)
                
                
                
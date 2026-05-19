def solution(N, stages):
    answer =[]
    total = len(stages)
    
    for i in range(1,N+1):
        current_stage= stages.count(i)
        
        if total>0:
            failrate = current_stage/total
            answer.append((i,failrate))
            total -= current_stage
        else:
            answer.append((i,0))

    answer.sort(key=lambda x: (-x[1],x[0]))
    
    return [a for a,b in answer]
def solution(answers):
    peo1 = [1, 2, 3, 4, 5]
    peo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    peo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct1 = 0
    correct2 = 0
    correct3 = 0
    
    for i in range(len(answers)):
        if peo1[i % len(peo1)] == answers[i]:
            correct1 += 1
        if peo2[i % len(peo2)] == answers[i]: 
            correct2 += 1
        if peo3[i % len(peo3)] == answers[i]:
            correct3 += 1
            
    max_score = max(correct1, correct2, correct3)  
    scores = [correct1, correct2, correct3]
    
    answer = [idx+1 for idx,score in enumerate(scores) if score==max_score]
    
    return answer
def solution(k, m, score):
    sorted_score = sorted(score,reverse=True)
    result = 0
    for i in range(0,len(score)-len(score)%m,m):
        box = sorted_score[i:i+m]
        
        result += min(box)*m
    return result
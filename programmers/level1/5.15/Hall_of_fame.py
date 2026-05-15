def solution(k, score):
    answer = []
    fame = []
    for s in score:
        fame.append(s)
        fame.sort(reverse=True)
        if len(fame)>k:
            fame.pop()
        
        answer.append(fame[-1])
        
    return answer
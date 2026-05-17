def solution(a, b):
    day=[31,29,31,30,31,30,31,31,30,31,30,31]
    week=['FRI','SAT','SUN','MON','TUE','WED','THU',]
    answer = []
    result = 0
    for i in range(366):
        answer.append(week[i%len(week)])
        
    for i in range(a-1):
        result += day[i]
    result += b
    
    return answer[result-1]
        
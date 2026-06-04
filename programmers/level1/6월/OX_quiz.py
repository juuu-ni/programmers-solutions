def solution(quiz):
    answer = []
    
    for q in quiz:
        parts = q.split()
        
        X = int(parts[0])
        operator = parts[1]
        Y = int(parts[2])
        Z = int(parts[4])
        
        if operator == '+':
            real_result = X + Y
        elif operator == '-':
            real_result = X - Y
            
        if real_result == Z:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer
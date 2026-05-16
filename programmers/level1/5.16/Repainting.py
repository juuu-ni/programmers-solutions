def solution(n, m, section):
    count = 0
    paint = 0
    
    for s in section:
        if s > paint:
            count += 1
            paint = s + m - 1 
            
    return count
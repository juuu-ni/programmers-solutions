def solution(sides):
    a, b = sorted(sides)
    case1 = b - (b - a)
    case2 = (a + b) - b - 1
    
    return case1 + case2
def solution(balls, share):
    up = 1
    down = 1
    for i in range(share):
        up *= balls-i
        
    for i in range(1,share+1):
        down *= i
        
    return up // down
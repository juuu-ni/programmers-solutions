def solution(keyinput, board):
    result = [0,0]
    max_x = board[0]//2
    max_y = board[1]//2
    
    for cord in keyinput:
        if cord == "left":
            if result[0] > -max_x:
                result[0]-=1
        elif cord == "right":
            if result[0] < max_x:
                result[0]+=1
        elif cord == "up":
            if result[1] < max_y:
                result[1]+=1
        elif cord == "down":
            if result[1] > -max_y:
                result[1]-=1
                
    return result
                        
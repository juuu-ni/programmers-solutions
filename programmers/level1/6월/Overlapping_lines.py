def solution(lines):
    count = [0] * 200
    for a,b in lines:
        for i in range(a+100,b+100):
            count[i] +=1
            
    return sum(1 for i in count if i>=2)
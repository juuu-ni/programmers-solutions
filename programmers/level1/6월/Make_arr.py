def solution(l, r):
    answer = []
    
    while l%5!=0:
        l+=1
        
    for i in range(l,r+1,5):
        for c in str(i):
            if c!= '0' and c!= '5' :
                break
        else:
            answer.append(i)
            
    return sorted(answer) if answer else [-1]
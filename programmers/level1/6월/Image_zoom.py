def solution(picture, k):
    answer = []
    for i in picture:
        new = ''
        for chr in i:
            new += chr * k
            
        for _ in range(k):
            answer.append(new)
    return answer
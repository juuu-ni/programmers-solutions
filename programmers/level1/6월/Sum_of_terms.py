def solution(a, d, included):
    arr=[a+d*i for i in range(len(included))]
    
    answer = 0
    for i,j in zip(included,arr):
        if i:
            answer+=j
    return answer
            
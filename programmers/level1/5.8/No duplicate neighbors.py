def solution(arr):
    answer = []
    for value in arr:
        if not answer or answer[-1] != value:
            answer.append(value)
            
    return answer
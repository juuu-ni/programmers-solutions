def solution(array):
    many = [0] * (max(array)+1)
    for i in array:
        many[i]+=1
        
    return many.index(max(many)) if many.count(max(many)) ==1 else -1
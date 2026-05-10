def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if budget<i:
            return count
        count+=1
        budget-=i
    return count
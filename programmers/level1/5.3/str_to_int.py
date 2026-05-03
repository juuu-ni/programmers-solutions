def solution(s):
    return s+ sum([i for i in range(1,(s//2)+1) if num %i==0])
print(solution(12))
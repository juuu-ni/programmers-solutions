def solution(lottos, win_nums):
    count = 0
    zeros = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
    for i in win_nums:
        if i in lottos:
            count+=1
            
    best = zeros + count
    worst = count
    return [rank[best],rank[worst]]
   
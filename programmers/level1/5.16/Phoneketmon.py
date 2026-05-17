def solution(nums):
    pick = len(nums)//2
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    
    return min(pick,len(result))
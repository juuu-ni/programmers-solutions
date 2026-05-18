from itertools import combinations
def solution(nums):
    result = 0
    for a,b,c in combinations(nums,3):
        total= a+b+c
        is_prime=True
        for i in range(2,int(total**0.5)+1):
            if total%i==0:
                is_prime=False
                break
        if is_prime:
            result +=1
        
    return result
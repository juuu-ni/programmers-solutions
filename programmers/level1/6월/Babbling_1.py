from itertools import permutations
def solution(babbling):
    bal = ["aya","ye","woo","ma"]
    result = 0

    for a,b in permutations(bal,2):
        bal.append(a+b)
    
    for a,b,c in permutations(bal,3):
        bal.append(a+b+c)
    
    for i in babbling:
        if i in bal:
            result += 1
            
    return result
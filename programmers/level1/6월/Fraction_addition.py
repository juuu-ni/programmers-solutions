def solution(numer1, denom1, numer2, denom2):
    if max(denom1, denom2) % min(denom1, denom2) != 0:
        denom = denom1 * denom2
        numer = (numer1 * denom2) + (numer2 * denom1)
    else:
        denom = max(denom1, denom2)
        if denom1 == denom:
            n = denom // denom2
            numer = numer1 + (numer2 * n)
        else:
            n = denom // denom1
            numer = numer2 + (numer1 * n)
            
    a = numer
    b = denom
    while b != 0:
        a, b = b, a % b
    gcd = a 
    
    return [numer // gcd, denom // gcd]
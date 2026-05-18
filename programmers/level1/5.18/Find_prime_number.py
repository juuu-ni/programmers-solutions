def is_prime(num):
    for i in range(2,int(num**(0.5))+1):
        if num%i==0:
            return False
    return True

def solution(n):
    result = 0
    for j in range(2,n+1):
        if is_prime(j):
            result+=1
    return result
                
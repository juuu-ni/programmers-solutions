def solution(chicken):
    service = 0  
    coupons = chicken 
    
    while coupons >= 10:
        new_chicken = coupons // 10 
        service += new_chicken        
        
        coupons = new_chicken + (coupons % 10)
        
    return service
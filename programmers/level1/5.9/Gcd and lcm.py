def solution(n, m):
    n_fact = [i for i in range(1, n+1) if n % i == 0]
    m_fact = [i for i in range(1,m+1) if m %i==0]
    
    common =[]
    for i in n_fact:
        if i in m_fact:
            common.append(i)
    
    gcd = max(common)
    lcm = n * m // gcd
    
    return [gcd, lcm]
def solution(a, b, c, d):
    lst=sorted([a,b,c,d])
    count = set(lst)
    
    if len(count)==1:
        p = lst[0]
        return 1111*p
    elif len(count)==2:
        if lst[0]==lst[2] or lst[1] == lst[3]:
            p = lst[1]
            q = lst[3] if lst[0]==lst[2] else lst[0]
            return (10*p+q)**2
        else:
            p = lst[1]
            q = lst[2]
            return (p+q)*abs(p-q)
    elif len(count)==3:
        for i in lst:
            if lst.count(i)==2:
                count.remove(i)
                break
        q,r=list(count)
        return q*r
    else:
        return min(lst)
def solution(n):
    lst = []
    while True:
        if n // 3 ==0:
            lst.append(n)
            break
        rest = n%3
        lst.append(rest)
        n = n//3
        
    new_lst=[]
    for i in range(len(lst)):
        new_lst.append(lst[i]*3**(len(lst)-(i+1)))
    return sum(new_lst)
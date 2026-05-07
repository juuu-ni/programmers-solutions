def solution(n):
    lst = []
    for i in range(n):
        if i%2==0:
            lst.append('수')
        else:
            lst.append('박')
    
    answer = ''.join(lst)
    return answer
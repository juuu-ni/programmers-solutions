def solution(a, b):
    lst = []
    if a<b:
        for i in range(a,b+1):
            lst.append(i)
    elif a>b:
        for i in range(b,a+1):
            lst.append(i)
    else:
        lst.append(a)
    answer = sum(lst)
    return answer

def solution(X, Y):
    count_X=[0]*10
    lst=[]
    
    for x in X:
        count_X[int(x)]+=1
    
    for y in Y:
        y_int = int(y)
        if count_X[y_int]>0:
            lst.append(y)
            count_X[y_int]-=1
    
    lst.sort(reverse=True)
    
    if not lst:
        return "-1"
    elif lst[0]=="0":
        return "0"
    else :
        return ''.join(lst)
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i]==False:
            absolutes[i]= -absolutes[i]
    
    lst=[]
    for i in range(len(absolutes)):
        lst.append(absolutes[i])
    
    answer=sum(lst)
    return answer
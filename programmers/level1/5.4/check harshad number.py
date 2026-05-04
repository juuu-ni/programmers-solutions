def solution(x):
    arr = list(str(x))
    sum_num = 0
    for i in range(len(arr)):
        sum_num += int(arr[i])
        
    if x%sum_num==0:
        return True
    else:
        return False
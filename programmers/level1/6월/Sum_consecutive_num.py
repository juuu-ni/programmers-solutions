def solution(num, total):
    result = []
    cnt = 0
    sum = 0
    for i in range(0,num):
        sum += cnt
        cnt += 1
    n = int((total-sum)/num)
    for i in range(0,num):
        result.append(n+i)
    return result
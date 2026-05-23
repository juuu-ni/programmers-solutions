def solution(numbers):
    lst = [0,1,2,3,4,5,6,7,8,9]
    result = 0
    for i in lst:
        if i not in numbers:
            result += i
    return result
def solution(numbers):
    num_lst = [0,1,2,3,4,5,6,7,8,9]
    sum_lst = []
    for i in range(len(numbers)):
        if numbers[i] in num_lst:
            sum_lst.append(numbers[i])
        
    difference = list(set(num_lst)-set(sum_lst))
    sum_num = sum(difference)
    return sum_num
 
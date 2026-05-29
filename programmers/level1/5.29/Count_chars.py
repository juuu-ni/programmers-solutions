def solution(my_string):
    result = [0]*52
    for i in my_string:
        if i.isupper():
            index = ord(i)- ord("A")
            result[index] +=1
        else:
            index = ord(i) - ord("a") + 26
            result[index] += 1
    return result
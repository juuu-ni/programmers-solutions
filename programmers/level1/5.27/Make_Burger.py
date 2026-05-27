def solution(ingredient):
    ham = []
    count = 0
    for i in ingredient:
        ham.append(i)
        
        if ham[-4:]==[1,2,3,1]:
            del ham[-4:]
            count += 1
    return count